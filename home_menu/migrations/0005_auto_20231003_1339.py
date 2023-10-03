# Generated by Django 3.2.15 on 2023-10-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_menu', '0004_subscription_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='allergy',
            field=models.ManyToManyField(blank=True, to='home_menu.Allergy', verbose_name='Аллергия'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='dish',
            field=models.ManyToManyField(to='home_menu.Dish', verbose_name='Блюда'),
        ),
    ]
