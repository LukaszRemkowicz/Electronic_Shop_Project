import datetime
from typing import Any, Dict

from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.utils import timezone
from django.db import ProgrammingError

from Articles.models import LandingPageArticles
from ProductApp.models import MainProductDatabase as Products, ProductOfTheDayDB
from Profile.forms import CustomLoginForm
from ProductApp.utilss.view_utils import change_product_pieces
from .models import ContentBase

CATTEGORIES = ["Laptops", "Phones", "PC", "Monitors",
               "Accesories for laptops", "SSD",
               "Graphs", "Ram", "Pendrives", "Routers",
               "Switches", "Motherboard", "CPU",
               "TV", "Headphones"]


class LandingPage(FormView):
    form_class = CustomLoginForm
    template_name = 'Landingpage/landing_page.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('account')

    def form_valid(self, form):
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        user = authenticate(self.request, email=email, password=password)

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

        # TODO return product of the day even if promotion ended. Think about productOfTheDay history model. Is it worth?

        context = super(LandingPage, self).get_context_data(**kwargs)
        cattegories = [product_cat for product_cat in CATTEGORIES]

        articles = list(LandingPageArticles.objects.filter(outdated=False))[:3]
        selected = Products.objects.filter(selected=True)
        try:
            product_of_the_day = Products.objects.filter(
                product_of_the_day=True
            ).last()
            localtime = timezone.template_localtime(
                product_of_the_day.product_of_the_day_added
            )
            product_of_the_day.product_of_the_day_added = localtime
            product_of_the_day.save()

        except (IndexError, ProgrammingError, AttributeError) as e:
            product_of_the_day = ''
            print(e)
            pass

        if product_of_the_day:
            date = timezone.now() - datetime.timedelta(days=7)
            product_of_the_day = Products.objects.filter(
                product_of_the_day_added__gte=date,
                product_of_the_day=True
            ).last()
            localtime = timezone.template_localtime(
                product_of_the_day.product_of_the_day_added)
            product_of_the_day.product_of_the_day_added = localtime
            product_of_the_day.save()

        else:
            product_of_the_day = ProductOfTheDayDB.objects.all().order_by('-date_start').first()
            if product_of_the_day:
                product_of_the_day = Products.objects.get(id=product_of_the_day.product.id)

        try:
            promotion_pieces = {product: change_product_pieces(
                self.request, product)[0] for product in selected}
        except ProgrammingError:
            promotion_pieces = ''

        context['product_of_the_day'] = product_of_the_day
        context['promotion_pieces'] = promotion_pieces
        context['selected'] = selected
        context['articles'] = articles
        context['cattegories'] = cattegories

        return context


class DeliveryPage(ListView):
    template_name = 'Landingpage/delivery.html'
    model = ContentBase


class InstallmentsPage(ListView):
    template_name = 'Landingpage/installments.html'
    model = ContentBase


class InsurancePage(ListView):
    template_name = 'Landingpage/insurance.html'
    model = ContentBase


class AssemblyPage(ListView):
    template_name = 'Landingpage/assembly.html'
    model = ContentBase


class ReturnsComplaintsPage(ListView):
    template_name = 'Landingpage/returnsComplaints.html'
    model = ContentBase


class FrequentlyQuestionsPage(ListView):
    template_name = 'Landingpage/frequentlyQuestions.html'
    model = ContentBase


class AboutPage(ListView):
    template_name = 'Landingpage/about.html'
    model = ContentBase


class RegulationsPage(ListView):
    template_name = 'Landingpage/regulations.html'
    model = ContentBase


class PrivacyPolicyPage(ListView):
    template_name = 'Landingpage/privacyPolicy.html'
    model = ContentBase


class CareerPage(ListView):
    template_name = 'Landingpage/career.html'
    model = ContentBase


class ContactPage(ListView):
    template_name = 'Landingpage/contact.html'
    model = ContentBase
