from django import forms
from .models import LandingPageArticles, ArticleComment
from mptt.forms import TreeNodeChoiceField


class BlogAdminForm(forms.ModelForm):
    content_wysiwyg = forms.CharField(
        widget=forms.Textarea(attrs={"id": "richtext_field"})
    )

    class Meta:
        model = LandingPageArticles
        fields = "__all__"


class ArticleComents(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=ArticleComment.objects.all())

    class Meta:
        model = ArticleComment
        fields = [
            "comment",
            "name",
            "email",
            "parent",
        ]
