from typing import Any
import os
import codecs

from django.db import models
from django.utils.safestring import mark_safe


class ContentBase(models.Model):
    delivery = models.FileField(
        upload_to="products_pic", default="", null=True, blank=True
    )

    def render_html(self) -> Any:
        path = self.delivery.path
        if os.path.exists(path):
            html_string = codecs.open(path, "r").read()
            return mark_safe(html_string)
        return None
