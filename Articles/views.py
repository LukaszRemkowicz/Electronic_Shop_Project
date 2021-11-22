from django.shortcuts import render
from django.views.generic import ListView
from . import models


class LandingArticles(ListView):
    template_name = 'landingPage/blog.html'
    model = models.LandingPageArticles
