# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-28 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True  # 第一次创建， create table语句

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='标题')),
                ('describe', models.CharField(max_length=100, verbose_name='描述')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
                'db_table': 't_tag',
                'ordering': ['-add_time'],
            },
        ),
    ]
