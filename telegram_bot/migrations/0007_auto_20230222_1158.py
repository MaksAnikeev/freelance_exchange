# Generated by Django 3.2.12 on 2023-02-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0006_auto_20230222_1153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tariff',
            options={'verbose_name': 'Тариф', 'verbose_name_plural': 'Тарифы'},
        ),
        migrations.AlterField(
            model_name='client',
            name='end',
            field=models.DateField(blank=True, default=2, null=True, verbose_name='Дата конца тарифа'),
        ),
    ]
