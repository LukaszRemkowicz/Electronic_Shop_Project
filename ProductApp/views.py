from typing import Any, Dict

from django.views.generic import ListView
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from ShoppingCardApp.models import Customer, Order, OrderItem
from . import models
from .utils import filter_products, sort_by_product_rate, paginate_view

User = settings.AUTH_USER_MODEL


class ProductPage(ListView):
    template_name = 'productapp/product.html'
    model = models.MainProductDatabase

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(ProductPage, self).get_context_data(**kwargs)
        product_id = self.kwargs['MainProductDatabase_id']
        product =  models.MainProductDatabase.objects.get(id=product_id)

        try:
            customer = Customer.objects.get(user=self.request.user)
            order = Order.objects.get(customer=customer, complete=False)
            order_item = OrderItem.objects.get(order=order)
            pieces = product.pieces - order_item.quantity

        except ObjectDoesNotExist:
            order_item = ''
            pieces = product.pieces

        same_products = filter_products(product.cattegory, product)
        # print('same_products', same_products)

        if pieces <= 10:
            pieces_range = range(1, pieces+1)
        else:
            pieces_range = range(1, 11)

        reviews = models.Reviews.objects.filter(product_id=product_id, checked_by_employer=True)
        question = models.Questions.objects.filter(product_id=product_id, checked_by_employer=True)

        context['questions'] = question
        context['reviews'] = reviews
        context['pieces_range'] = pieces_range
        context['same_products'] = same_products
        context['product'] = product
        context['pieces'] = pieces

        return context

class ProductsCart(ListView):
    template_name = 'productapp/product_cart.html'
    model =  models.MainProductDatabase

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(ProductsCart, self).get_context_data(**kwargs)
        product_cattegory = self.kwargs['cattegory']
        products =  models.MainProductDatabase.objects.filter(cattegory=product_cattegory)
        context['products_total'] = len(products)

        if self.request.GET.get('filter'):
            filter_option = self.request.GET.get('filter')
            choose_param = {
                'popular': sort_by_product_rate(products),
                'trending': products.order_by('-bought_num'),
                'cheapest': products.order_by('price'),
                'latest': products
            }

            try:
                products = choose_param[filter_option]
                context['products_total'] = len(products)

            except ObjectDoesNotExist:
                pass

            context['filter_option'] = filter_option

        context['products_total'] = len(products)
        page = self.request.GET.get('page')
        result = 9

        ranger, paginator, products = paginate_view(products, result, page)

        context['page_num_range'] = range(paginator.num_pages-3, paginator.num_pages+1)
        context['last_page'] = paginator.num_pages
        context['custom_range'] = ranger
        context['cattegory'] = product_cattegory
        context['paginator'] = paginator
        context['products'] = products

        return context
