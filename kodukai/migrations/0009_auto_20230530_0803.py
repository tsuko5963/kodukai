# Generated by Django 3.2.19 on 2023-05-29 23:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kodukai', '0008_alter_treasurer_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treasurer',
            name='amount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='treasurer',
            name='credit',
            field=models.CharField(choices=[('b', '銀行'), ('c', 'カード'), ('g', '現金'), ('d', '借金'), ('s', 'スイカ'), ('k', '収入'), ('t', '立替'), ('d', '引当金'), ('p', 'ペイペイ')], max_length=1, verbose_name='勘定'),
        ),
        migrations.AlterField(
            model_name='treasurer',
            name='debit',
            field=models.CharField(choices=[('b', '銀行'), ('c', 'カード'), ('g', '現金'), ('d', '借金'), ('s', 'スイカ'), ('k', '費用'), ('t', '立替'), ('d', '引当金'), ('p', 'ペイペイ')], max_length=1, verbose_name='勘定'),
        ),
    ]
