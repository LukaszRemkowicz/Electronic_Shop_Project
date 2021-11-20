from typing import Any, Dict
import json

from django.views.generic import ListView
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from ShoppingCardApp.models import Customer, Order, OrderItem
# from . import models
from .utils import filter_products, sort_by_product_rate, paginate_view, try_to_get_product
from .utilss.view_utils import *
from .filters import SnippetFilter
from ProductApp import models

# TODO change productApp models. Add "as"

User = settings.AUTH_USER_MODEL


class ProductPage(ListView):
    template_name = 'productapp/product.html'
    model = models.MainProductDatabase

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(ProductPage, self).get_context_data(**kwargs)
        product_id = self.kwargs['MainProductDatabase_id']
        product = models.MainProductDatabase.objects.get(id=product_id)

        # if self.request.user.is_authenticated:
        #     customer = Customer.objects.get(user=self.request.user)
        #     order = Order.objects.get(customer=customer, complete=False)
        #     try:
        #         order_item = OrderItem.objects.get(order=order, product__ean=product.ean)
        #         pieces = product.pieces - order_item.quantity

        #     except ObjectDoesNotExist:
        #         order_item = ''
        #         pieces = product.pieces

        # elif not self.request.user.is_authenticated:
        #     order_item = ''
        #     pieces = product.pieces
            
        pieces, _ = change_product_pieces(self.request, product)
        same_products = filter_products(product.cattegory, product)
        # print('same_products', same_products)

        if pieces <= 10:
            pieces_range = range(1, pieces + 1)
        else:
            pieces_range = range(1, 11)

        product = try_to_get_product(product, '')

        reviews = models.Reviews.objects.filter(product_id=product_id, checked_by_employer=True)
        question = models.Questions.objects.filter(product_id=product_id, checked_by_employer=True)

        print('same products', same_products)
        context['questions'] = question
        context['reviews'] = reviews
        context['pieces_range'] = pieces_range
        context['same_products'] = same_products
        context['product'] = product
        context['pieces'] = pieces

        return context


class ProductsCart(ListView):
    template_name = 'productapp/product_cart.html'
    model = models.MainProductDatabase

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """ View for render products in product_cart template.
        On this view products are filtered by user applied filters """

        # TODO: Write tests for this view

        context = super().get_context_data(**kwargs)

        if self.request.GET.get('ids'):
            products_old = get_similar_products_data(self.request)

        else:
            products_old = ''

        product_cattegory = self.kwargs['cattegory']
        old_products = models.MainProductDatabase.objects.filter(cattegory=product_cattegory)

        # Call the products models, filter by url queryset and return as query.

        cattegories = {
            'TV': lambda x: filter_tv_products(x),
            'Monitors': lambda x: filter_monitors_products(x),
            'PC': lambda x: filter_pcs_products(x),
            'SSD': lambda x: filter_ssd_products(x),
            'Graphs': lambda x: filter_graphs_products(x),
            'Ram': lambda x: filter_rams_products(x),
            'Pendrives': lambda x: filter_pendrives_products(x),
            'Switches': lambda x: filter_switches_products(x),
            'Motherboard': lambda x: filter_motherboard_products(x),
            'CPU': lambda x: filter_cpus_products(x),
            'Headphones': lambda x: filter_headphones_products(x),
            'Routers': lambda x: filter_routers_products(x),
            'Accesories for laptops': lambda x: filter_accesories_products(x),
            'Laptops': lambda x: filter_laptops_products(x),
            'Phones': lambda x: filter_phones_products(x),
        }

        try:
            products = cattegories[product_cattegory](self.request)
        except (KeyError, ObjectDoesNotExist):
            products = []

        # Filter products by popularity, trending filters etc.
        # Should be done at the end of all filters

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
                # print( [product.price for product in products])

            except ObjectDoesNotExist:
                pass

        # Method is called from specific produc Model.
        # Returning dictionary with filter name as a "key", and number of products as a "value".
        # For example: {'diagonal':2} == {filter:prodcut_number}.

        product_filters = try_to_get_product(old_products[0], '')
        try:
            data_to_filter = product_filters.data_products_to_filter()
        except IndexError:
            data_to_filter = []

        # Create producent dictionary {name: products number for producent}
        # from first query (all producents)

        old_products = [try_to_get_product(product, '') for product in old_products]
        producents = models.Inherit.get_producents(old_products)

        if self.request.GET.get('ids'):
            similar_products = get_similar_products_data(self.request)
            similar_products_ean = [product.ean for product in similar_products]
            products = products.filter(ean__in=similar_products_ean)
            params_excluded = ['filter', 'grid', 'page', 'ids']
            params_list = [key for key, _ in self.request.GET.lists() if key not in params_excluded]
            if params_list:
                data_to_filter = products_old[0].data_products_to_filter(products_old)
            else:
                data_to_filter = products[0].data_products_to_filter(products)

            producents = models.Inherit.get_producents(products)

            # print('product 0 ', products[0])
            # print('data_to_filter', data_to_filter)

        context['products_total'] = len(products)

        # Paginate View
        page = self.request.GET.get('page')
        result = 9
        ranger, paginator, products = paginate_view(products, result, page)

        # TODO: Think about using this filter
        form = SnippetFilter

        if self.request.GET.get('filter'):
            context['filter_option'] = self.request.GET.get('filter')

        context['products_filter_options'] = data_to_filter
        context['producents'] = producents
        context['page_num_range'] = range(paginator.num_pages - 3, paginator.num_pages + 1)
        context['last_page'] = paginator.num_pages
        context['custom_range'] = ranger
        context['cattegory'] = product_cattegory
        context['paginator'] = paginator
        context['products'] = products
        context['form'] = form
        context['mainDatabaseProd'] = old_products

        return context

# class CheckSimilar(ListView):
#     template_name = 'check_similar.html'
#     model =  models.MainProductDatabase


#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         """ View for render products in product_cart template.
#         On this view products are filtered by user applied filters """

#         #TODO: Write tests for this view

#         context = super().get_context_data(**kwargs)
#         url_params = { key:str(value[0]) for key, value in self.request.GET.lists()}
#         ids = json.loads(url_params['ids'])

#         products = MainProductDatabase.objects.all()

#         products = products.filter(id__in=ids)

#         print(products)

#         return context
