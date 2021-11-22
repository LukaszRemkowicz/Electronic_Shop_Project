from django.db import models


class LandingPageArticles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=3000)
    outdated = models.BooleanField(default=False)

    img = models.ImageField(upload_to='articles/landin-page', null=True, blank=True)
    second_img = models.ImageField(upload_to='articles/landin-page', null=True, blank=True)
    third_img = models.ImageField(upload_to='articles/landin-page', null=True, blank=True)
