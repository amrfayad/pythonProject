# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('mainPicture', models.ImageField(upload_to=b'')),
                ('text', models.CharField(max_length=10000)),
                ('pup_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('mainPicture', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('posts', models.ManyToManyField(to='posts.Post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Section'),
        ),
    ]