# Generated by Django 3.2.12 on 2023-02-24 17:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0024_auto_20230224_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='end',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 3, 24, 20, 18, 56, 303433), null=True, verbose_name='Дата конца тарифа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='dialogue',
            field=models.JSONField(blank=True, null=True, verbose_name='Переписка'),
        ),
        migrations.AlterField(
            model_name='order',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 24, 20, 18, 56, 304438), verbose_name='Опубликован'),
        ),
    ]
