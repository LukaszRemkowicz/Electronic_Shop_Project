import json
import datetime
import re
from django.core.exceptions import ObjectDoesNotExist

from django.http.response import JsonResponse
from rest_framework import serializers, generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib import messages

from .serializers import AuthTokenSerializer, UserSerializer
from ShoppingCardApp import utils  
from ShoppingCardApp import models as shopping_cart
from AddressBookApp import models as address
from ProductApp import models as product_app
from ProductApp.utils import find_new_product

class CreateUserView(generics.CreateAPIView):
    """ create user """
    serializer_class = UserSerializer

    
class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user
    
    
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
            order, created = shopping_cart.Order.objects.get_or_create(customer=customer, complete=False)
            
        else:
            customer, order = utils.complete_unauthorised_user_order(request, data)
            
         
        total = float(data['price']) 
        # print('total: ', total)
        # print('get_cart_total', order.get_cart_total)   
        order.transaction_id = transaction_id 
        
        if total == float(order.get_cart_total):
            order.complete = True
        order.save()
        
        products =shopping_cart.OrderItem.objects.filter(order=order)
        for item in products:
            item.product.pieces -= item.quantity
            item.product.save()
   
        shopping_cart.ShippingAddress.objects.create(
            customer = customer,
            order = order,
            address = data['customerStreet'],
            city = data['customerCity'],
            state = data['customerState'],
            zipcode = data['customerZipcode'], 
        )
        
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
        order, created = shopping_cart.Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = shopping_cart.OrderItem.objects.get_or_create(order=order, product=product)
        
        if action == 'add':
            orderItem.quantity = (orderItem.quantity + int(amount))
        elif action == 'remove':
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
        
        print('tutaj', product_parametr)
        
        re_pattern = r'(.*-)(.*)(-.*)'

        product_parametr = re.match(re_pattern, product_parametr).group(2)
        main_product = product_app.MainProductDatabase.objects.get(id=int(main_product))
                
        # if product_parametr == 'memory'  or product_parametr == 'battery':
        #     product_data = int(product_data[:-4])
        # elif product_parametr == 'ram':
        #     product_data = int(product_data[:-3])
 
        product = find_new_product(product_items_list, product_data, product_parametr, main_product)
                
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
            messages.info(request, 'Review has been saved')
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
        
        question = product_app.Questions.objects.create(product_id=int(product_id),
                                                        question=content,
                                                        user=request.user)

        result = {'result' : 'Question sent. Wait for our employer reply'}
        return Response(json.dumps(result))