from django.shortcuts import render
from django.http import JsonResponse

import json

from ProductApp.models import MainProductDatabase 

def update_item(request):
    data = json.loads(request.data)
    product_id = data['productId']
    action = data['action']
    
    customer = request.user.customer
    product = MainProductDatabase.objects.get(id=product_id)
    return JsonResponse("item was added", safe=False)