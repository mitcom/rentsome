# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 20:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
            preserve_default=False,
        ),
    ]
