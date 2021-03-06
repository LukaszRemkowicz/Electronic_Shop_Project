from typing import Any, Dict

from django.views.generic import CreateView

from Landingpage.utils.url_path import get_url_path
from . import models
from . import forms


class LandingArticles(CreateView):
    template_name = "Articles/blog.html"
    model = models.LandingPageArticles
    form_class = forms.ArticleComents

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(LandingArticles, self).get_context_data(**kwargs)
        article_id = self.kwargs["article_id"]
        article = models.LandingPageArticles.objects.get(id=article_id)
        comments = models.ArticleComment.objects.filter(article__id=article_id)

        context["url_last"], context["url_path"] = get_url_path(self.request)
        context["comments_number"] = len(comments)
        context["article"] = article
        context["comments"] = models.ArticleComment.objects.filter(article=article)

        # Paginator
        # page = self.request.GET.get('page', 1)
        # result = 5
        # ranger, paginator, products = paginate_view(comments, result, page)

        return context
