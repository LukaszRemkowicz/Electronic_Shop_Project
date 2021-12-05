from typing import Any, Dict

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from Articles.models import LandingPageArticles
from ProductApp.models import MainProductDatabase as Products
from Profile.forms import CustomLoginForm
from .models import ContentBase

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


class DeliveryPage(ListView):

    template_name = 'delivery.html'
    model = ContentBase

class InstallmentsPage(ListView):

    template_name = 'installments.html'
    model = ContentBase

class InsurancePage(ListView):

    template_name = 'insurance.html'
    model = ContentBase

class AssemblyPage(ListView):

    template_name = 'assembly.html'
    model = ContentBase
    
    
class ReturnsComplaintsPage(ListView):

    template_name = 'returnsComplaints.html'
    model = ContentBase
    
    
class FrequentlyQuestionsPage(ListView):

    template_name = 'frequentlyQuestions.html'
    model = ContentBase
    

class AboutPage(ListView):

    template_name = 'about.html'
    model = ContentBase
    

class RegulationsPage(ListView):

    template_name = 'regulations.html'
    model = ContentBase
    
    
class PrivacyPolicyPage(ListView):

    template_name = 'privacyPolicy.html'
    model = ContentBase
    
    
class CareerPage(ListView):

    template_name = 'career.html'
    model = ContentBase
    
    
class ContactPage(ListView):

    template_name = 'contact.html'
    model = ContentBase
