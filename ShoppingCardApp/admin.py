from django.contrib import admin

from .models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ['date_order', 'id']

admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(ShoppingCard)

