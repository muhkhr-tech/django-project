# Generated by Django 4.2.11 on 2024-03-07 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belanjainaja', '0004_shoppingitem_shopping_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping',
            name='total_price',
            field=models.BigIntegerField(default=0),
        ),
    ]
