# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0003_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image_height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='image_width',
            field=models.IntegerField(null=True),
        ),
    ]
