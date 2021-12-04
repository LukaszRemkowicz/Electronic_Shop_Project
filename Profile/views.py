from typing import Any, Dict

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth import authenticate
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.views import View
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from Articles.models import LandingPageArticles
from ProductApp.models import MainProductDatabase as Products

from .forms import RegisterForm, AcceptTerms, CustomLoginForm
from .models import Profile


CATTEGORIES = ["Laptops", "Phones", "PC", "Monitors","Accesories for laptops", "SSD",
           "Graphs", "Ram", "Pendrives", "Routers", "Switches", "Motherboard", "CPU",
           "TV", "Headphones"]


class LandingPage(FormView):
    form_class = CustomLoginForm
    template_name = 'landing_page.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('account')

    def form_valid(self, form):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            messages.info(self.request, "You have logged in")
        else:
            messages.error(self.request, "Username or password incorrect")


        return super(LandingPage, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)

        return redirect('landing-page')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(LandingPage, self).get_context_data(**kwargs)
        cattegories = [product_cat for product_cat in CATTEGORIES]
        
        articles = LandingPageArticles.objects.filter(outdated=False)[:3]
        selected = Products.objects.filter(selected=True)
        product_of_the_day = Products.objects.filter(product_of_the_day=True)[0]
        
        context['product_of_the_day'] = product_of_the_day
        context['selected'] = selected
        context['articles'] = articles
        context['cattegories'] = cattegories

        return context


class UserAccount(LoginRequiredMixin, FormView):
    model = Profile
    form_class = CustomLoginForm
    template_name= 'profile/account.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('account')


class Register(FormView):
    template_name = 'profile/register.html'
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

