# Generated by Django 3.2 on 2021-12-28 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Articles", "0004_auto_20211224_2332"),
    ]

    operations = [
        migrations.AlterField(
            model_name="landingpagearticles",
            name="img",
            field=models.ImageField(
                blank=True, null=True, upload_to="articles/landin-page/2021-12-28"
            ),
        ),
        migrations.AlterField(
            model_name="landingpagearticles",
            name="second_img",
            field=models.ImageField(
                blank=True, null=True, upload_to="articles/landin-page/2021-12-28"
            ),
        ),
        migrations.AlterField(
            model_name="landingpagearticles",
            name="tempalate",
            field=models.FileField(
                blank=True, default="", null=True, upload_to="articles/blogs/2021-12-28"
            ),
        ),
        migrations.AlterField(
            model_name="landingpagearticles",
            name="third_img",
            field=models.ImageField(
                blank=True, null=True, upload_to="articles/landin-page/2021-12-28"
            ),
        ),
    ]
