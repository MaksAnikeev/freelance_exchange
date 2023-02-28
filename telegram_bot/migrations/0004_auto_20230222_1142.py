# Generated by Django 3.2.12 on 2023-02-22 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0003_alter_administrator_chat_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.PositiveBigIntegerField(verbose_name='ID чата в ТГ')),
                ('tariff', models.CharField(choices=[('Cheap', 'Эконом'), ('Standart', 'Стандарт'), ('VIP', 'VIP')], max_length=256, verbose_name='Тариф')),
                ('end', models.DateField(default=2, verbose_name='Дата конца тарифа')),
            ],
        ),
        migrations.AlterModelOptions(
            name='administrator',
            options={'verbose_name': 'Администратор', 'verbose_name_plural': 'Администраторы'},
        ),
    ]
