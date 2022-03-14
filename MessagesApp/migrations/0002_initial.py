# Generated by Django 3.2 on 2021-12-22 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ShoppingCardApp', '0001_initial'),
        ('MessagesApp', '0001_initial'),
        ('ProductApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='complaint',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ShoppingCardApp.order'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ProductApp.mainproductdatabase'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]