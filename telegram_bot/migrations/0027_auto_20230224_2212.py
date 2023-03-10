# Generated by Django 3.2.12 on 2023-02-24 19:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0026_auto_20230224_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='files',
            field=models.JSONField(default=[], verbose_name='Файлы'),
        ),
        migrations.AlterField(
            model_name='client',
            name='end',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 3, 24, 22, 12, 21, 209539), null=True, verbose_name='Дата конца тарифа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 24, 22, 12, 21, 225174), verbose_name='Опубликован'),
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
