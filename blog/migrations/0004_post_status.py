# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160225_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'0', b'Draft'), (b'1', b'Published'), (b'2', b'Not Published')]),
        ),
    ]
