# Generated by Django 3.2 on 2022-01-19 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Articles", "0011_auto_20220117_1931"),
    ]

    operations = [
        migrations.AlterField(
            model_name="landingpagearticles",
            name="img",
            field=models.ImageField(
                blank=True, null=True, upload_to="articles/landin-page/2022-01-19"
            ),
        ),
        migrations.AlterField(
            model_name="landingpagearticles",
            name="second_img",
            field=models.ImageField(
                blank=True, null=True, upload_to="articles/landin-page/2022-01-19"
            ),
        ),
        migrations.AlterField(
            model_name="landingpagearticles",
            name="tempalate",
            field=models.FileField(
                blank=True, default="", null=True, upload_to="articles/blogs/2022-01-19"
            ),
        ),
        migrations.AlterField(
            model_name="landingpagearticles",
            name="third_img",
            field=models.ImageField(
                blank=True, null=True, upload_to="articles/landin-page/2022-01-19"
            ),
        ),
    ]
