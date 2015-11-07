# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0014_participant_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=20, blank=True, default=''),
            preserve_default=False,
        ),
    ]
