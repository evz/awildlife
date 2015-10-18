# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0006_auto_20151017_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='price',
        ),
        migrations.AddField(
            model_name='event',
            name='price_lower',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='price_upper',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(to='life.Participant', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
