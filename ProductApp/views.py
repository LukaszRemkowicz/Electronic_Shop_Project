from typing import Any, Dict
import json

from django.views.generic import ListView, FormView
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpRequest, request

from ShoppingCardApp.models import Customer, Order, OrderItem
from . import models
from .utils import filter_products, sort_by_product_rate, paginate_view, try_to_get_product
from .utilss.view_utils import *
from .forms import FilterForm
from .filters import SnippetFilter
from ProductApp import models

User = settings.AUTH_USER_MODEL


class ProductPage(ListView):
    template_name = 'productapp/product.html'
    model = models.MainProductDatabase

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(ProductPage, self).get_context_data(**kwargs)
        product_id = self.kwargs['MainProductDatabase_id']
        product =  models.MainProductDatabase.objects.get(id=product_id)

        if self.request.user.is_authenticated:
            customer = Customer.objects.get(user=self.request.user)
            order = Order.objects.get(customer=customer, complete=False)
            try:
                order_item = OrderItem.objects.get(order=order, product__ean=product.ean)
                pieces = product.pieces - order_item.quantity

            except ObjectDoesNotExist:
                order_item = ''
                pieces = product.pieces

        elif not self.request.user.is_authenticated:
            order_item = ''
            pieces = product.pieces

        same_products = filter_products(product.cattegory, product)
        # print('same_products', same_products)

        if pieces <= 10:
            pieces_range = range(1, pieces+1)
        else:
            pieces_range = range(1, 11)

        product = try_to_get_product(product, '')


        reviews = models.Reviews.objects.filter(product_id=product_id, checked_by_employer=True)
        question = models.Questions.objects.filter(product_id=product_id, checked_by_employer=True)

        context['questions'] = question
        context['reviews'] = reviews
        context['pieces_range'] = pieces_range
        context['same_products'] = same_products
        context['product'] = product
        context['pieces'] = pieces

        return context

# class ProductsCart(ListView):
#     template_name = 'productapp/product_cart.html'
#     model =  models.MainProductDatabase

#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         context = super(ProductsCart, self).get_context_data(**kwargs)
#         product_cattegory = self.kwargs['cattegory']
#         products =  models.MainProductDatabase.objects.filter(cattegory=product_cattegory)
#         context['products_total'] = len(products)

#         print(self.request.GET.get('filter'))

#         if self.request.GET.get('filter'):
#             filter_option = self.request.GET.get('filter')
#             choose_param = {
#                 'popular': sort_by_product_rate(products),
#                 'trending': products.order_by('-bought_num'),
#                 'cheapest': products.order_by('price'),
#                 'latest': products
#             }

#             try:
#                 products = choose_param[filter_option]
#                 context['products_total'] = len(products)

#             except ObjectDoesNotExist:
#                 pass

#             context['filter_option'] = filter_option

#         context['products_total'] = len(products)
#         page = self.request.GET.get('page')
#         result = 9

#         """ Create producent dictionary {name: products number for producent}"""
#         product_data = [try_to_get_product(product, '') for product in products]
#         producent_dictionary = {}
#         for product in product_data:
#             if product.producent in producent_dictionary:
#                 producent_dictionary[product.producent] += 1
#             else:
#                 producent_dictionary[product.producent] = 1


#         """ Paginate View """
#         ranger, paginator, products = paginate_view(products, result, page)

#         """ Get data to filter """
#         data_to_filter = product_data[0].data_products_to_filter()
#         print(producent_dictionary)

#         context['products_filter_options'] = data_to_filter
#         context['producents'] = producent_dictionary
#         context['page_num_range'] = range(paginator.num_pages-3, paginator.num_pages+1)
#         context['last_page'] = paginator.num_pages
#         context['custom_range'] = ranger
#         context['cattegory'] = product_cattegory
#         context['paginator'] = paginator
#         context['products'] = products

#         return context


class ProductsCart(ListView):
    template_name = 'productapp/product_cart.html'
    model =  models.MainProductDatabase


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """ View for render products in product_cart template.
        On this view products are filtered by user applied filters """

        #TODO: Write tests for this view

        context = super().get_context_data(**kwargs)

        product_cattegory = self.kwargs['cattegory']
        old_products =  models.MainProductDatabase.objects.filter(cattegory=product_cattegory)

        # Call the products models, filter by url queryset and return as query.

        #TODO: add filters by cattegory. Create functions for each model

        cattegories = {
            'TV':  filter_tv_products(self.request)
        }

        try:
            products = cattegories[product_cattegory]
        except (KeyError, ObjectDoesNotExist) as e:
            products = []


        # Filter products by popular, trending filters etc.
        # It should be done at the end of all filters

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

            context['filter_option'] = filter_option


        # Method is called from specific produc Model.
        # Returning dictionary with filter name as a "key", and number of products as a "value".
        # For example: {'diagonal':2} == {filter:prodcut_number}.

        #TODO: add data_products_to_filter method to each model. Add try catch blocks

        try:
            data_to_filter = products[0].data_products_to_filter()
        except IndexError:
            data_to_filter = []

        print(data_to_filter)


        # Create producent dictionary {name: products number for producent}
        # from first query (all producents)

        old_products = [try_to_get_product(product, '') for product in old_products]

        context['products_total'] = len(products)

        # Paginate View
        page = self.request.GET.get('page')
        result = 9
        ranger, paginator, products = paginate_view(products, result, page)


        #TODO: Think about using this filter
        form = SnippetFilter

        context['products_filter_options'] = data_to_filter
        context['producents'] = models.Inherit.get_producents(old_products)
        context['page_num_range'] = range(paginator.num_pages-3, paginator.num_pages+1)
        context['last_page'] = paginator.num_pages
        context['custom_range'] = ranger
        context['cattegory'] = product_cattegory
        context['paginator'] = paginator
        context['products'] = products
        context['form'] = form
        context['mainDatabaseProd'] = old_products

        return context


