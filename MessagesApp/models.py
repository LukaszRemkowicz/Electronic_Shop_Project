from django.db import models


class Message(models.Model):
    user_id = models.IntegerField(blank=False)
    message = models.CharField(max_length=10000)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.message
