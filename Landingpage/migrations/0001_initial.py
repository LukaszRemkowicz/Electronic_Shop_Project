# Generated by Django 3.2 on 2021-12-22 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContentBase",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "delivery",
                    models.FileField(
                        blank=True, default="", null=True, upload_to="products_pic"
                    ),
                ),
            ],
        ),
    ]
