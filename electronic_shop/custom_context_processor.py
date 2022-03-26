from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from Profile.forms import CustomLoginForm, KeepMeLoggedIn
from ShoppingCardApp.models import Order, Customer
from ShoppingCardApp.utils import order_cart
from ProductApp.models import MainProductDatabase, ProductOfTheDayDB


def login_form_content(request):
    form = CustomLoginForm()
    keep_me = KeepMeLoggedIn()

    if request.user.is_authenticated:
        try:
            customer = Customer.objects.get(user=request.user.id)
            order = Order.objects.get(customer=customer, transaction_status=False)

        except ObjectDoesNotExist:
            customer = ""
            order = ""

        try:
            likes = MainProductDatabase.objects.filter(likes=request.user).count()
        except ObjectDoesNotExist:
            likes = ""

    else:
        _, order, _ = order_cart(request)
        likes = ""

    product_of_the_day = MainProductDatabase.objects.filter(
        product_of_the_day=True
    ).order_by("-product_of_the_day_added")

    if len(product_of_the_day) >= 1:
        product_of_the_day = product_of_the_day[0]
        localtime = timezone.template_localtime(
            product_of_the_day.product_of_the_day_added
        )
        product_of_the_day.product_of_the_day_added = localtime
        product_of_the_day.save()
    else:
        product_of_the_day_db = (
            ProductOfTheDayDB.objects.all().order_by("-date_start").first()
        )
        if product_of_the_day_db:

            product_of_the_day = MainProductDatabase.objects.get(
                id=product_of_the_day.product.id
            )

    return {
        "login_form": form,
        "keep_me": keep_me,
        "order": order,
        "likes": likes,
        "product_of_the_day": product_of_the_day,
    }
