# Generated by Django 3.2 on 2022-02-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0009_alter_productofthedaydb_date_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productofthedaydb',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
