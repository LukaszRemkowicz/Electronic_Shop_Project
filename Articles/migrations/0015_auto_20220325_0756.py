# Generated by Django 3.2 on 2022-03-25 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Articles", "0014_auto_20220216_0840"),
    ]

    operations = [
        migrations.AlterField(
            model_name="landingpagearticles",
            name="img",
            field=models.ImageField(
                blank=True, null=True, upload_to="articles/landin-page/2022-03-25"
            ),
        ),
        migrations.AlterField(
            model_name="landingpagearticles",
            name="second_img",
            field=models.ImageField(
                blank=True, null=True, upload_to="articles/landin-page/2022-03-25"
            ),
        ),
        migrations.AlterField(
            model_name="landingpagearticles",
            name="tempalate",
            field=models.FileField(
                blank=True, default="", null=True, upload_to="articles/blogs/2022-03-25"
            ),
        ),
        migrations.AlterField(
            model_name="landingpagearticles",
            name="third_img",
            field=models.ImageField(
                blank=True, null=True, upload_to="articles/landin-page/2022-03-25"
            ),
        ),
    ]
