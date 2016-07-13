# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_poems'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='post_image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('0', 'Draft'), ('1', 'Published'), ('2', 'Not Published')], default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
