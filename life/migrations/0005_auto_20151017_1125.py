# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0004_auto_20151017_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(max_length=255, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
    ]
