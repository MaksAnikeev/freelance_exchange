# Generated by Django 3.2.12 on 2023-02-24 17:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0023_auto_20230224_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='end',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 3, 24, 20, 17, 49, 55902), null=True, verbose_name='Дата конца тарифа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='dialogue',
            field=models.TextField(blank=True, null=True, verbose_name='Переписка'),
        ),
        migrations.AlterField(
            model_name='order',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 24, 20, 17, 49, 55902), verbose_name='Опубликован'),
        ),
    ]