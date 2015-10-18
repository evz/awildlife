# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0005_auto_20151017_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventbrite_url',
            field=models.URLField(blank=True, null=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(width_field='image_width', blank=True, null=True, upload_to='', height_field='image_height'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image_height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='image_width',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, to='life.Participant'),
        ),
    ]
