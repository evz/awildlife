# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import recurrence.fields


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0007_auto_20151018_0900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_time',
        ),
        migrations.AddField(
            model_name='event',
            name='schedule',
            field=recurrence.fields.RecurrenceField(null=True),
        ),
    ]
