# Generated by Django 3.2 on 2022-02-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ProductApp", "0008_productofthedaydb"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productofthedaydb",
            name="date_start",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
