from django.contrib import admin
from . import models
from . import forms
from mptt.admin import MPTTModelAdmin

class BlogAdmin(admin.ModelAdmin):
    form = forms.BlogAdminForm

admin.site.register(models.LandingPageArticles, BlogAdmin)
admin.site.register(models.ArticleComment, MPTTModelAdmin)
