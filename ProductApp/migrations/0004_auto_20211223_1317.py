# Generated by Django 3.2 on 2021-12-23 12:17

import ProductApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ProductApp", "0003_auto_20211222_2335"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mainproductdatabase",
            name="main_photo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=ProductApp.models.product_image_file_path,
            ),
        ),
        migrations.AlterField(
            model_name="mainproductdatabase",
            name="second_photo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=ProductApp.models.product_image_file_path,
            ),
        ),
        migrations.AlterField(
            model_name="mainproductdatabase",
            name="third_photo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=ProductApp.models.product_image_file_path,
            ),
        ),
    ]
