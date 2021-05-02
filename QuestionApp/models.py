from django.db import models


class Question(models.Model):
    subject = models.CharField(blank=True, max_length=20)
    question_text = models.CharField(blank=True, max_length=1000)
    date = models.DateField(auto_now_add=True)
    user_id = models.IntegerField()

    CHOICES = [
        ("Answered", "Answered"),
        ("Readed", "Readed"),
        ("Closed", "Closed")
    ]

    state = models.CharField(max_length=50, choices=CHOICES)

    def __str__(self):
        return self.subject

