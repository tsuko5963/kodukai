# Generated by Django 3.2.19 on 2023-05-20 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Kanjo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kanjo', models.CharField(max_length=1)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Treasurer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_date', models.DateTimeField()),
                ('item', models.CharField(max_length=20)),
                ('debit', models.CharField(max_length=1)),
                ('credit', models.CharField(max_length=1)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Valid_date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_date', models.DateTimeField()),
            ],
        ),
    ]
