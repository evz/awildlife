# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0002_auto_20151017_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(null=True, height_field='image_height', width_field='image_width', upload_to=''),
        ),
    ]
