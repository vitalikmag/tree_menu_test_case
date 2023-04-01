# Generated by Django 4.1.7 on 2023-03-31 13:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Имя')),
                ('names', models.CharField(blank=True, max_length=101, verbose_name='Имя множества')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, verbose_name='Имя')),
                ('path', models.CharField(blank=True, max_length=256, verbose_name='Путь')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu_app.category',
                                               verbose_name='Категория')),
                ('parent',
                 models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT,
                                   to='menu_app.menu', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Запись в меню',
                'verbose_name_plural': 'Записи в меню',
            },
        ),
    ]
