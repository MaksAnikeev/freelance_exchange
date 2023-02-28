# Generated by Django 3.2.12 on 2023-02-22 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0013_auto_20230222_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariff',
            name='description',
            field=models.TextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='end',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 3, 22, 17, 44, 49, 794271), null=True, verbose_name='Дата конца тарифа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 22, 17, 44, 49, 796373), verbose_name='Опубликован'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='title',
            field=models.CharField(max_length=256, unique=True, verbose_name='Название'),
        ),
    ]
