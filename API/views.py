import json
import datetime
from django.http.response import JsonResponse

from rest_framework import serializers, generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .serializers import AuthTokenSerializer, UserSerializer
from ShoppingCardApp import utils  
from ShoppingCardApp import models as shopping_cart
from AddressBookApp import models as address
from ProductApp import models as product_app

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
    
    def post(self, request):
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]
        parser_classes = [JSONParser]
        
        items, order, cart_items = utils.order_cart(request)
        context = {'items': items, 'order': order}
        
        return Response(json.dumps(context, cls=utils.DecimalEncoder))
    
    
class FinishOrderView(APIView):
    """ finish order api """
    
    def post(self, request, format=None) -> JsonResponse:
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
    
    def post(self, request):
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAdminUser]
        parser_classes = [JSONParser]
        
        data = request.data
        product_id = data['productId']
        action = data['action']
        
        # customer = request.user.customer
        try:
            customer = request.user.customer
        except:
            customer = shopping_cart.Customer.objects.create(user=request.user)
            customer.email = request.user.email
            customer.save()
        
        product = product_app.MainProductDatabase.objects.get(id=product_id)
        order, created = shopping_cart.Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = shopping_cart.OrderItem.objects.get_or_create(order=order, product=product)
        
        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)
        elif action == 'delete':
            orderItem.quantity = 0
            
        orderItem.save()
        
        if orderItem.quantity <= 0:
            orderItem.delete()
            
        data = {
            'items' : orderItem.quantity,
            'summaryItem': orderItem.get_total,
            'subtotal': order.get_cart_total,
            'totalItems': order.get_cart_items,
        }
        
        return Response(json.dumps(data, cls=utils.DecimalEncoder))