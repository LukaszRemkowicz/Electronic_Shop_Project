from typing import Any, Dict

from django.shortcuts import render
from django.views.generic import ListView
from . import models


class LandingArticles(ListView):
    template_name = 'landingPage/blog.html'
    model = models.LandingPageArticles

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(LandingArticles, self).get_context_data(**kwargs)
        article_id = self.kwargs['article_id']
        
        context['article'] = models.LandingPageArticles.objects.get(id=article_id)
        print(context['article'])
        print('*'*100)
        print('model', self.model)
        print('*'*100)
        print(context)
        return context