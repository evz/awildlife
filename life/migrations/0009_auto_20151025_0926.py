# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0008_auto_20151025_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
