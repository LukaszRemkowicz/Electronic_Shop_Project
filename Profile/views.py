from typing import Any, Dict

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.urls import resolve

from ProductApp.models import MainProductDatabase
from .forms import RegisterForm, AcceptTerms, CustomLoginForm
from .models import Profile
from ShoppingCardApp.models import Order, OrderItem
from Landingpage.utils.url_path import get_url_path


class UserAccount(LoginRequiredMixin, FormView):
    model = Profile
    form_class = CustomLoginForm
    template_name= 'Profile/orders.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('account')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['url_last'], context['url_path'] = get_url_path(self.request)

        orders = Order.objects.filter(customer__user=self.request.user, transaction_status=True).order_by('-transaction_finished')

        context['orders'] = orders

        return context


class DetailOrder(ListView):
    model = OrderItem
    template_name = 'Profile/order-detail-view.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        items = self.model.objects.filter(order=self.kwargs['order_id']).order_by('-date_ordered')

        context['url_last'], context['url_path'] = get_url_path(self.request)

        context['order_item'] = items

        return context


class Register(FormView):
    template_name = 'Profile/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('landing-page')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        accepted_terms = AcceptTerms()
        context['register_form'] = context.get('register_form')
        context['accepted_terms'] = accepted_terms
        return context

    def form_valid(self, form):
        user = form.save()

        if user is not None:
            login(self.request, user)
            messages.info(self.request, "account created")

        return super(Register, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)

        return super(Register, self).form_invalid(form)

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('landing-page')
        return super().get(request, *args, **kwargs)

