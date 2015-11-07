# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0015_auto_20151031_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, null=True, max_length=20),
        ),
    ]
