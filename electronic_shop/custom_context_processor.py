from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.utils.deprecation import MiddlewareMixin

from Profile.forms import CustomLoginForm, KeepMeLoggedIn
from ShoppingCardApp.models import Order, Customer
from ShoppingCardApp.utils import order_cart


def login_form_content(request):
    form = CustomLoginForm()
    keep_me = KeepMeLoggedIn()

    if request.user.is_authenticated:
        try:
            customer = Customer.objects.get(user=request.user.id)
            order = Order.objects.get(customer=customer, complete=False)
        except:
            customer = ''
            order = ''
    else:
        _, order, _ = order_cart(request)

    return {'login_form': form, 'keep_me': keep_me, 'order': order}




