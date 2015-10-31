# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0013_auto_20151025_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='phone',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
