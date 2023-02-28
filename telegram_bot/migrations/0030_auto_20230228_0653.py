# Generated by Django 3.2.12 on 2023-02-28 03:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0029_alter_client_end_alter_order_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='end',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 3, 28, 6, 53, 6, 617785), null=True, verbose_name='Дата конца тарифа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 28, 6, 53, 6, 618785), verbose_name='Опубликован'),
        ),
    ]