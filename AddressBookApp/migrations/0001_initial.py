# Generated by Django 3.2 on 2021-12-22 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AddressBook",
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
                ("name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=50)),
                ("street", models.CharField(default="", max_length=100)),
                ("post_code", models.CharField(max_length=10)),
                ("state", models.CharField(blank=True, max_length=30)),
                ("phone_number", models.CharField(max_length=15)),
                ("default", models.BooleanField(default=False)),
            ],
        ),
    ]
