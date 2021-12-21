import os
from typing import Any
import codecs
from datetime import datetime
import time

from django.db import models
from django.conf import settings
from django.db.models.fields import related
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel, TreeForeignKey

User = settings.AUTH_USER_MODEL


class LandingPageArticles(models.Model):

    title = models.CharField(max_length=100)
    outdated = models.BooleanField(default=False)
    tag_one = models.CharField(max_length=20, default='', blank=True, null=True)
    tag_two = models.CharField(max_length=20, default='', blank=True, null=True)
    tag_three = models.CharField(max_length=20, default='', blank=True, null=True)
    alt_short_descript = models.CharField(max_length=100, default='', blank=True, null=True)
    posted = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content_wysiwyg = models.TextField()
    short_description = models.CharField(max_length=100)
    img = models.ImageField(upload_to=f"articles/landin-page/{time.strftime('%Y-%m-%d')}", null=True, blank=True)
    second_img = models.ImageField(upload_to=f"articles/landin-page/{time.strftime('%Y-%m-%d')}", null=True, blank=True)
    third_img = models.ImageField(upload_to=f"articles/landin-page/{time.strftime('%Y-%m-%d')}", null=True, blank=True)

    tempalate = models.FileField(upload_to=f"articles/blogs/{time.strftime('%Y-%m-%d')}", default="", null=True, blank=True)

    def __str__(self) -> str:
        return f'Blog id: {self.id}, posted: {self.posted} {self.title[:20]}..'

    @property
    def render_template(self) -> Any:
        path = self.tempalate.path
        if os.path.exists(path):
            html_string = codecs.open(path, 'r').read()
            return mark_safe(html_string)
        return None

    @property
    def render_content(self) -> Any:
        path = self.content.path
        if os.path.exists(path):
            html_string = codecs.open(path, 'r').read()
            return mark_safe(html_string)
        return None

    @property
    def when_posted(self) -> str:
        user_name = self.owner.first_name if self.owner.first_name else ''
        last_name = self.owner.last_name if self.owner.last_name else ''

        owner = f'{user_name} {last_name}' if user_name and last_name else 'Unknown'

        return f'Posted on {self.posted.strftime("%B")} {self.posted.day}, {self.posted.year} by {owner}'

    @property
    def return_tags(self) -> list:
        listed = []
        if self.tag_one:
            listed.append(self.tag_one)
        if self.tag_two:
            listed.append(self.tag_two)
        if self.tag_three:
            listed.append(self.tag_three)

        return listed


class ArticleComment(MPTTModel):

    article = models.ForeignKey(LandingPageArticles, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    email = models.CharField(max_length=100)
    publish = models.DateField(auto_now_add=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=50)
    checked = models.BooleanField(default=False)

    class MPTTMeta:
        order_insertion_by = ['publish']

    def __str__(self):
        return f'{self.name} Comment ID: {self.id}'
