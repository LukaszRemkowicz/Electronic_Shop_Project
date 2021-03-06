# Generated by Django 3.2 on 2021-12-22 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Complaint",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(default="RMA", max_length=20)),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("In progress", "In progress"),
                            ("Sent", "Sent"),
                            ("Closed", "Closed"),
                        ],
                        default="checking the complaint",
                        max_length=50,
                    ),
                ),
                ("message", models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(default="Question", max_length=300)),
                ("subject", models.CharField(blank=True, max_length=20)),
                ("message", models.CharField(max_length=10000)),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("Answered", "Answered"),
                            ("Readed", "Readed"),
                            ("Closed", "Closed"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
    ]
