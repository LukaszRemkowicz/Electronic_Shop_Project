from django.contrib import admin
from . import models

admin.site.register(models.MainProductDatabase)
admin.site.register(models.Phones)
admin.site.register(models.Monitors)
admin.site.register(models.Reviews)
admin.site.register(models.Questions)