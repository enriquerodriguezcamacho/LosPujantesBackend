# Generated by Django 5.1.7 on 2025-04-09 16:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_category_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='stock',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
