from typing import Any, Dict
from django.core.paginator import Paginator

from django.shortcuts import render
from django.views.generic import ListView, CreateView

from ProductApp.utils import paginate_view
from . import models
from . import forms


class LandingArticles(CreateView):
    template_name = 'landingPage/blog.html'
    model = models.LandingPageArticles
    form_class = forms.ArticleComents

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(LandingArticles, self).get_context_data(**kwargs)
        article_id = self.kwargs['article_id']
        article = models.LandingPageArticles.objects.get(id=article_id)
        comments = models.ArticleComment.objects.filter(article__id=article_id)
        context['comments_number'] = len(comments)
        context['article'] = article
        context['comments'] = models.ArticleComment.objects.filter(article=article)
        
        # Paginator
        # page = self.request.GET.get('page', 1)
        # result = 5
        # ranger, paginator, products = paginate_view(comments, result, page)
 
        return context