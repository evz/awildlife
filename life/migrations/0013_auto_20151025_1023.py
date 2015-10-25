# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0012_auto_20151025_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='registrations',
        ),
        migrations.AddField(
            model_name='registration',
            name='participant',
            field=models.ForeignKey(null=True, to='life.Participant'),
        ),
    ]
