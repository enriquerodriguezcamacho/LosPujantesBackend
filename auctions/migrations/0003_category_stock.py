# Generated by Django 5.1.7 on 2025-04-09 16:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='stock',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
    ]
