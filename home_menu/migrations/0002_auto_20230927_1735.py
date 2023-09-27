# Generated by Django 3.2.15 on 2023-09-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.IntegerField(verbose_name='Количество грамм'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='promo_code',
            field=models.ManyToManyField(blank=True, to='home_menu.PromotionalCode', verbose_name='Промо-код'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='allergy',
            field=models.ManyToManyField(blank=True, to='home_menu.Allergy', verbose_name='Аллергия'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='promo_code',
            field=models.ManyToManyField(blank=True, to='home_menu.PromotionalCode', verbose_name='Промо-код'),
        ),
    ]
