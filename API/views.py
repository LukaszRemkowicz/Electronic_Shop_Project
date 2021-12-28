import json
import datetime
from math import prod
import os
import re
from decimal import Decimal
import time

from django.core.files import File
from django.http.response import JsonResponse
from django.views import generic
from rest_framework import serializers, generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib import messages
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

# from Profile.models import Profile
from .serializers import AuthTokenSerializer, BlogArticlesSerializer, CreateProductSerializer, GetQuantitySerializer, NewsletterSerializer, ProductSerializer, ProfileSerializer, UserSerializer
from ShoppingCardApp import utils
from ShoppingCardApp import models as shopping_cart
from AddressBookApp import models as address
from ProductApp import models as product_app
from ProductApp.utils import find_new_product
from .utils import change_model_to_dict

User = get_user_model()

class CreateUserView(generics.CreateAPIView):
    """ create user """
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def _clean_data(self, data):
        if isinstance(data, bytes):
            data = data.decode(errors='ignore')
        return super(CreateTokenView, self)._clean_data(data)


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user


class ManageProfileView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated Profile"""
    serializer_class = ProfileSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication Profile"""
        profile = User.objects.get(user=self.request.user.id)

        return profile


class UnauthorisedUserOrderView(APIView):
    """ created order and items for unauthorised user """

    def post(self, request) -> Response:
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]
        parser_classes = [JSONParser]

        items, order, cart_items = utils.order_cart(request)
        context = {'items': items, 'order': order}

        return Response(json.dumps(context, cls=utils.DecimalEncoder))


class FinishOrderView(APIView):
    """ finish order api """

    def post(self, request, format=None) -> Response:
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]
        parser_classes = [JSONParser]

        data = request.data
        payment_method = data['payment']
        transaction_id = datetime.datetime.now().timestamp()

        if request.user.is_authenticated:
            customer = request.user.customer
            try:
                order, created = shopping_cart.Order.objects.get_or_create(customer=customer, transaction_status=False)
            except MultipleObjectsReturned:
                order = shopping_cart.Order.objects.filter(customer=customer, transaction_status=False).order_by('-date_order')[0]
        else:
            customer, order = utils.complete_unauthorised_user_order(request, data)


        total = float(data['price'])
        # print('total: ', total)
        # print('get_cart_total', order.get_cart_total)
        order.transaction_id = transaction_id

        if total == float(order.get_cart_total):
            order.transaction_status = True
            order.transaction_finished = datetime.datetime.now()
        order.save()

        products =shopping_cart.OrderItem.objects.filter(order=order)
        for item in products:


            if item.quantity > item.product.pieces:
                if order.transaction_status:
                    item.bought = item.product.pieces
                    item.product.bought_num += item.product.pieces
                    item.save()
                item.product.pieces -=  item.product.pieces

            else:
                if order.transaction_status:
                    item.bought = item.quantity
                    item.product.bought_num += item.quantity
                item.product.pieces -= item.quantity
                item.status = 'Collected'
                item.save()

            # item.product.pieces -= item.quantity
            item.product.save()

        shopping_cart.ShippingAddress.objects.create(
            customer = customer,
            order = order,
            address = data['customerStreet'],
            city = data['customerCity'],
            state = data['customerState'],
            zipcode = data['customerZipcode'],
        )

        # time.sleep(50000)
        return Response('Order saved..')


class UpdateItemView(APIView):
    """ Update item quantity """

    def post(self, request) -> Response:
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]
        parser_classes = [JSONParser]

        data = request.data

        product_id = data['productId']
        action = data['action']
        amount = data['amount']

        # customer = request.user.customer
        try:
            customer = request.user.customer
        except:
            customer = shopping_cart.Customer.objects.create(user=request.user, email=request.user.email)
            customer.email = request.user.email
            customer.save()

        product = product_app.MainProductDatabase.objects.get(id=product_id)
        order = shopping_cart.Order.objects.filter(customer=customer, transaction_status=False)
        print(order)
        try:
            order, created = shopping_cart.Order.objects.get_or_create(customer=customer, transaction_status=False)
        except MultipleObjectsReturned:
            order = order.order_by('-date_order')[0]

        orderItem, created = shopping_cart.OrderItem.objects.get_or_create(order=order, product=product)

        if action == 'add':
            if orderItem.quantity + int(amount) >= product.pieces:
                orderItem.quantity = product.pieces
            else:
                orderItem.quantity = (orderItem.quantity + int(amount))
        elif action == 'remove':
            if orderItem.quantity - int(amount) <= 0:
                orderItem.quantity = 0
            else:
                orderItem.quantity = (orderItem.quantity - int(amount))
        elif action == 'delete':
            orderItem.quantity = 0

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()

        product_quantity = product.pieces - orderItem.quantity

        data = {
            'items' : orderItem.quantity,
            'summaryItem': orderItem.get_total,
            'subtotal': order.get_cart_total,
            'totalItems': order.get_cart_items,
            'pieces': product_quantity
        }

        return Response(json.dumps(data, cls=utils.DecimalEncoder))

class GetProductData(APIView):

    def post(self, request)-> Response:
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]
        parser_classes = [JSONParser]

        data = request.data

        main_product = data['productData']['productId']
        product_items_list = data['productData']['itemsId']
        product_data = data['productData']['productClicked']['type']
        product_parametr = data['productData']['productClicked']['divId']

        # print('tutaj', product_parametr)
        # print('jakas lista', product_items_list)
        # print('product data' , product_data)

        re_pattern = r'(.*-)(.*)(-.*)'

        product_parametr = re.match(re_pattern, product_parametr).group(2)
        # print('Product-param', product_parametr)
        main_product = product_app.MainProductDatabase.objects.get(id=int(main_product))
        product = find_new_product(product_items_list, product_data, product_parametr, main_product)

        # print('nowy product', product)

        try:
            product_id = product.id

        except AttributeError:
            product_id = ''

        return Response(json.dumps(product_id))


class CreateReview(APIView):

    def post(self, request) -> Response:
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]
        parser_classes = [JSONParser]

        data = request.data

        content = data['content']
        product_id = data['productId']
        order_number = data['orderNumber']
        stars = data['stars']

        try:
            order = shopping_cart.Order.objects.get(id=int(order_number))
            order_item = shopping_cart.OrderItem.objects.get(order=order, product_id=int(product_id))
            new_review = product_app.Reviews.objects.create(product_id=int(product_id),
                                                            review=content,
                                                            user=request.user,
                                                            stars=stars)
            result = 'Review has been saved'
            messages.info(request, 'Review has been sent')
        except:
            result = f'This product have not been bought in order number {order_number}'
            messages.error(request, f'Wrong order number. Review has not been sent')

        response = {'result': result}
        return Response(json.dumps(response))


class CreateQuestion(APIView):

    def post(self, request) -> Response:
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]
        parser_classes = [JSONParser]

        data = request.data

        content = data['content']

        product_id = data['productId']
        name = data['name']

        try:
            question = product_app.Questions.objects.create(product_id=int(product_id),
                                                        question=content,
                                                        user=request.user,
                                                        name=name)
            messages.info(request, 'Question has been sent')
        except:
            messages.error(request, f'Something went wrong. Try again later')

        result = {'result' : 'Question sent. Wait for our employer reply'}
        return Response(json.dumps(result))

class ProductDict(APIView):
    def post(self, request) -> Response:
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]
        parser_classes = [JSONParser]

        data = request.data

        product_id = data['productId']

        try:
            product = product_app.MainProductDatabase.objects.get(id=int(product_id))
            product = change_model_to_dict(product)
        except ObjectDoesNotExist:
            return 'Object does not exist'

        print(product)

        return Response(json.dumps(product))

# class UpdateProduct(APIView):
#     def post(self, request, product_id) -> Response:
#         authentication_classes = [authentication.TokenAuthentication]
#         permission_classes = [permissions.IsAdminUser]
#         parser_classes = [JSONParser]

#         data = request.data
#         user_id = data['user_id']
#         print(data['fields'].items())
#         for field, value in data['fields'].items():
#             product = product_app.MainProductDatabase.objects.get(id=product_id)
#             user = User.objects.get(id=int(user_id))
#             gettattr = getattr(product, field)
#             if field == 'likes' and value == 'add':
#                 gettattr.add(user)
#             elif field == 'likes' and value == 'remove':
#                 gettattr.remove(user)


#         return Response('Product Updated')


class UpdateBlogComment(generics.CreateAPIView):
    serializer_class = BlogArticlesSerializer


class ProductView(generics.RetrieveUpdateAPIView):

    serializer_class = ProductSerializer
    queryset  = product_app.MainProductDatabase

    def patch(self, request, *args, **kwargs):
        """ Add/remove like attribute for product """

        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]
        parser_classes = [JSONParser]

        data = request.data
        user_id = data['user_id']
        product = self.queryset.get(id=kwargs['product_id'])
        user = User.objects.get(id=int(user_id))
        for field, value in data['fields'].items():
            gettattr = getattr(product, field)
            if field == 'likes' and value == 'add':
                gettattr.add(user)
            elif field == 'likes' and value == 'remove':
                gettattr.remove(user)
            else:
                # gettattr = value
                setattr(product, field, value)
                product.save()
        serializer_class = ProductSerializer(instance=product)

        return Response(serializer_class.data)

    def get_object(self):
        """Retrieve and return product"""

        if self.queryset.objects.all().count() >= 2:
            try:
                product = get_object_or_404(self.queryset, pk=self.kwargs['product_id'])
            except (ObjectDoesNotExist, IndexError):
                pass
            return product


class Newsletter(generics.CreateAPIView):
    """ Save email to newsletter database """

    serializer_class = NewsletterSerializer

    data = {"response": "Address has been added"}


class OrderProductQuantity(generics.ListAPIView):
    """ Get product pieces in basket """

    serializer_class = GetQuantitySerializer
    queryset  = shopping_cart.Order.objects.all()

    def get(self, request, *args, **kwargs):
        id = kwargs['product_id']

        try:
            product_item = shopping_cart.OrderItem.objects.filter(product__id=id, order__transaction_status=False)[0]
            product_item = product_item.quantity
        except IndexError:
            product_item = ''

        product_stock = product_app.MainProductDatabase.objects.get(id=id).pieces

        return Response({'order_quantity': product_item, 'product_stock': product_stock})



class CreateProduct(generics.CreateAPIView):

    serializer_class = CreateProductSerializer

    def post(self, request, *args, **kwargs):

        models = {
            'phones': lambda **item: product_app.Phones.objects.create(**item),
            'monitors': lambda **item: product_app.Monitors.objects.create(**item),
            'laptops': lambda **item: product_app.Laptops.objects.create(**item),
            'pcs': lambda **item: product_app.Pc.objects.create(**item),
            'accesories': lambda **item: product_app.AccesoriesForLaptops.objects.create(**item),
            'ssds': lambda **item: product_app.Ssd.objects.create(**item),
            'graphs': lambda **item: product_app.Graphs.objects.create(**item),
            'rams': lambda **item: product_app.Ram.objects.create(**item),
            'pendrives': lambda **item: product_app.Pendrives.objects.create(**item),
            'switches': lambda **item: product_app.Switches.objects.create(**item),
            'motherboards': lambda **item: product_app.Motherboard.objects.create(**item),
            'cpus': lambda **item: product_app.Cpu.objects.create(**item),
            'tvs': lambda **item: product_app.Tv.objects.create(**item),
            'headphones': lambda **item: product_app.Headphones.objects.create(**item),
            'routers': lambda **item: product_app.Routers.objects.create(**item),
        }

        fold = request.data
        PATH = rf'electronic_shop/electronic_shop/static/images/products/{fold["cattegory"].lower()}/'

        PATH = os.path.join(os.getcwd(), PATH).replace("\\","/")

        itt = models[fold["cattegory"].lower()](**fold)

        itt.main_photo.save(fold['main_photo'], File(open(PATH + fold['main_photo'], 'rb')))
        try:
            itt.second_photo.save(fold['second_photo'], File(open(PATH + fold['second_photo'], 'rb')))
        except:
            pass
        try:
            itt.third_photo.save(fold['third_photo'], File(open(PATH + fold['third_photo'], 'rb')))
        except:
            pass


        return super().post(request, *args, **kwargs)

