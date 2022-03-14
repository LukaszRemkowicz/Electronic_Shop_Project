import json
import datetime
import os
import re
from typing import Union

from django.core.files import File
from django.utils import timezone
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from . import serializers
from Articles.models import LandingPageArticles
from ShoppingCardApp import utils
from ShoppingCardApp import models as shopping_cart
from ProductApp import models as product_app
from ProductApp.utils import find_new_product
from .utils import change_model_to_dict
import Profile

User = get_user_model()


class CreateUserView(generics.CreateAPIView):
    """create user"""

    serializer_class = serializers.UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""

    serializer_class = serializers.AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def _clean_data(self, data):
        if isinstance(data, bytes):
            data = data.decode(errors="ignore")
        return super(CreateTokenView, self)._clean_data(data)


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""

    serializer_class = serializers.UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user


class ManageProfileView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated Profile"""

    serializer_class = serializers.ProfileSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication Profile"""
        profile = User.objects.get(user=self.request.user.id)

        return profile


class UnauthorisedUserOrderView(APIView):
    """created order and items for unauthorised user"""

    def post(self, request) -> Response:
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]
        parser_classes = [JSONParser]

        items, order, cart_items = utils.order_cart(request)
        context = {"items": items, "order": order}

        return Response(json.dumps(context, cls=utils.DecimalEncoder))


class FinishOrderView(APIView):
    """finish order api"""

    def post(self, request) -> Response:
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]
        parser_classes = [JSONParser]

        data = request.data
        payment_method = data["payment"]
        transaction_id = datetime.datetime.now().timestamp()

        if request.user.is_authenticated:
            customer = request.user.customer
            try:
                order, created = shopping_cart.Order.objects.get_or_create(
                    customer=customer, transaction_status=False
                )
            except MultipleObjectsReturned:
                order = shopping_cart.Order.objects.filter(
                    customer=customer, transaction_status=False
                ).order_by("-date_order")[0]
        else:
            customer, order = utils.complete_unauthorised_user_order(request, data)

        total = float(data["price"])
        order.transaction_id = transaction_id

        if total == float(order.get_cart_total):
            order.transaction_status = True
            order.transaction_finished = timezone.now()
        order.save()

        products = shopping_cart.OrderItem.objects.filter(order=order)
        for item in products:
            product_database = product_app.ProductOfTheDayDB.objects.filter(
                ean=item.product.ean
            ).last()

            if item.quantity > item.product.pieces:
                if order.transaction_status:
                    item.bought = item.product.pieces
                    item.product.bought_num += item.product.pieces
                    if product_database:
                        product_database.sold_num += item.product.pieces
                        product_database.save()
                    item.save()
                item.product.pieces -= item.product.pieces

            else:
                if order.transaction_status:
                    item.bought = item.quantity
                    item.product.bought_num += item.quantity
                    if product_database:
                        product_database.sold_num += item.quantity
                        product_database.save()

                item.product.pieces -= item.quantity
                item.status = "Collected"
                item.save()

            # item.product.pieces -= item.quantity
            item.product.save()

        shopping_cart.ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data["customerStreet"],
            city=data["customerCity"],
            state=data["customerState"],
            zipcode=data["customerZipcode"],
        )

        return Response("Order saved..")


class UpdateItemView(APIView):
    """Update item quantity"""

    def post(self, request) -> Response:
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]
        parser_classes = [JSONParser]

        data = request.data

        product_id = data["productId"]
        action = data["action"]
        amount = data["amount"]

        try:
            customer = request.user.customer
        except Profile.models.User.customer.DoesNotExist:
            customer = shopping_cart.Customer.objects.create(
                user=request.user, email=request.user.email
            )
            customer.email = request.user.email
            customer.save()

        product = product_app.MainProductDatabase.objects.get(id=product_id)
        order = shopping_cart.Order.objects.filter(
            customer=customer, transaction_status=False
        )
        try:
            order, created = shopping_cart.Order.objects.get_or_create(
                customer=customer, transaction_status=False
            )
        except MultipleObjectsReturned:
            order = order.order_by("-date_order")[0]

        orderItem, created = shopping_cart.OrderItem.objects.get_or_create(
            order=order, product=product
        )

        if action == "add":
            if orderItem.quantity + int(amount) >= product.pieces:
                orderItem.quantity = product.pieces
            else:
                orderItem.quantity = orderItem.quantity + int(amount)
        elif action == "remove":
            if orderItem.quantity - int(amount) <= 0:
                orderItem.quantity = 0
            else:
                orderItem.quantity = orderItem.quantity - int(amount)
        elif action == "delete":
            orderItem.quantity = 0

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()

        product_quantity = product.pieces - orderItem.quantity

        data = {
            "items": orderItem.quantity,
            "summaryItem": orderItem.get_total,
            "subtotal": order.get_cart_total,
            "totalItems": order.get_cart_items,
            "pieces": product_quantity,
        }

        return Response(json.dumps(data, cls=utils.DecimalEncoder))


class GetProductData(APIView):
    def post(self, request) -> Response:
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]
        parser_classes = [JSONParser]

        data = request.data

        main_product = data["productData"]["productId"]
        product_items_list = data["productData"]["itemsId"]
        product_data = data["productData"]["productClicked"]["type"]
        product_parametr = data["productData"]["productClicked"]["divId"]

        re_pattern = r"(.*-)(.*)(-.*)"

        product_parametr = re.match(re_pattern, product_parametr).group(2)
        main_product = product_app.MainProductDatabase.objects.get(id=int(main_product))
        product = find_new_product(
            product_items_list, product_data, product_parametr, main_product
        )

        try:
            product_id = product.id

        except AttributeError:
            product_id = ""

        return Response(json.dumps(product_id))


class CreateReview(APIView):
    def post(self, request) -> Response:
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]
        parser_classes = [JSONParser]

        data = request.data

        content = data["content"]
        product_id = data["productId"]
        order_number = data["orderNumber"]
        stars = data["stars"]

        try:
            order = shopping_cart.Order.objects.get(id=int(order_number))
            order_item = shopping_cart.OrderItem.objects.get(
                order=order, product_id=int(product_id)
            )
            product_app.Reviews.objects.create(
                product_id=int(product_id),
                review=content,
                user=request.user,
                stars=stars,
            )
            result = "Review has been saved"
            messages.info(request, "Review has been sent")
        except os.error:
            result = (
                f"This product have not been bought in order number " f"{order_number}"
            )
            messages.error(request, "Wrong order number. Review has not been sent")

        response = {"result": result}
        return Response(json.dumps(response))


class CreateQuestion(APIView):
    def post(self, request) -> Response:
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]
        parser_classes = [JSONParser]

        data = request.data

        content = data["content"]

        product_id = data["productId"]
        name = data["name"]

        try:
            product_app.Questions.objects.create(
                product_id=int(product_id),
                question=content,
                user=request.user,
                name=name,
            )
            messages.info(request, "Question has been sent")
        except os.error:
            messages.error(request, "Something went wrong. Try again later")

        result = {"result": "Question sent. Wait for our employer reply"}
        return Response(json.dumps(result))


class ProductDict(APIView):
    def post(self, request) -> Union[str, Response]:
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]
        parser_classes = [JSONParser]

        data = request.data

        product_id = data["productId"]

        try:
            product = product_app.MainProductDatabase.objects.get(id=int(product_id))
            product = change_model_to_dict(product)
        except ObjectDoesNotExist:
            return "Object does not exist"

        return Response(json.dumps(product))


class UpdateBlogComment(generics.CreateAPIView):
    serializer_class = serializers.BlogArticlesSerializer


class ProductView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = product_app.MainProductDatabase

    def patch(self, request, *args, **kwargs):
        """Add/remove like attribute for product"""

        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]
        parser_classes = [JSONParser]

        data = request.data
        user_id = data["user_id"]
        product = self.queryset.objects.get(id=kwargs["product_id"])
        user = User.objects.filter(id=int(user_id)).exists()
        for field, value in data["fields"].items():
            gettattr = getattr(product, field)
            if field == "likes" and value == "add":
                gettattr.add(user[0])
            elif field == "likes" and value == "remove":
                gettattr.remove(user[0])
            else:
                setattr(product, field, value)
                product.save()
        serializer_class = serializers.ProductSerializer(instance=product)

        return Response(serializer_class.data)

    def get_object(self):
        """Retrieve and return product"""

        product = ""

        if self.queryset.objects.all().count() >= 2:
            try:
                product = get_object_or_404(self.queryset, pk=self.kwargs["product_id"])
            except (ObjectDoesNotExist, IndexError):
                pass
            return product


class RetrievListOfProducts(generics.ListAPIView):
    """Get list of products"""

    serializer_class = serializers.RetrievProductsSerializer

    def get_queryset(self):
        ids = json.loads(self.kwargs["products_query"])
        queryset = LandingPageArticles.objects.all()
        result = queryset.filter(id__in=ids)

        return result


class Newsletter(generics.CreateAPIView):
    """Save email to newsletter database"""

    serializer_class = serializers.NewsletterSerializer

    data = {"response": "Address has been added"}


class OrderProductQuantity(generics.ListAPIView):
    """Get product pieces in basket"""

    serializer_class = serializers.GetQuantitySerializer
    queryset = shopping_cart.Order.objects.all()

    def get(self, request, *args, **kwargs):
        id = kwargs["product_id"]

        try:
            product_item = shopping_cart.OrderItem.objects.filter(
                product__id=id, order__transaction_status=False
            )[0]
            product_item = product_item.quantity
        except IndexError:
            product_item = ""

        product_stock = product_app.MainProductDatabase.objects.get(id=id).pieces

        return Response(
            {"order_quantity": product_item, "product_stock": product_stock}
        )


class CreateProduct(generics.CreateAPIView):
    serializer_class = serializers.CreateProductSerializer

    def post(self, request, *args, **kwargs):

        models = {
            "phones": lambda **item: product_app.Phones.objects.create(**item),
            "monitors": lambda **item: product_app.Monitors.objects.create(**item),
            "laptops": lambda **item: product_app.Laptops.objects.create(**item),
            "pcs": lambda **item: product_app.Pc.objects.create(**item),
            "accesories": lambda **item: product_app.AccesoriesForLaptops.objects.create(
                **item
            ),
            "ssds": lambda **item: product_app.Ssd.objects.create(**item),
            "graphs": lambda **item: product_app.Graphs.objects.create(**item),
            "rams": lambda **item: product_app.Ram.objects.create(**item),
            "pendrives": lambda **item: product_app.Pendrives.objects.create(**item),
            "switches": lambda **item: product_app.Switches.objects.create(**item),
            "motherboards": lambda **item: product_app.Motherboard.objects.create(
                **item
            ),
            "cpus": lambda **item: product_app.Cpu.objects.create(**item),
            "tvs": lambda **item: product_app.Tv.objects.create(**item),
            "headphones": lambda **item: product_app.Headphones.objects.create(**item),
            "routers": lambda **item: product_app.Routers.objects.create(**item),
        }

        fold = request.data
        path = rf'electronic_shop/electronic_shop/static/images/\
        products/{fold["cattegory"].lower()}/'

        path = os.path.join(os.getcwd(), path).replace("\\", "/")

        itt = models[fold["cattegory"].lower()](**fold)

        itt.main_photo.save(
            fold["main_photo"], File(open(path + fold["main_photo"], "rb"))
        )
        try:
            itt.second_photo.save(
                fold["second_photo"], File(open(path + fold["second_photo"], "rb"))
            )
        except os.error:
            pass
        try:
            itt.third_photo.save(
                fold["third_photo"], File(open(path + fold["third_photo"], "rb"))
            )
        except os.error:
            pass

        return super().post(request, *args, **kwargs)
