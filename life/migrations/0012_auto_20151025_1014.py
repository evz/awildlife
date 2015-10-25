# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0011_auto_20151025_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='event',
            field=models.ForeignKey(to='life.Event', null=True),
        ),
    ]
