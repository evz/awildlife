# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0010_auto_20151025_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('event_date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='participants',
        ),
        migrations.AddField(
            model_name='registration',
            name='event',
            field=models.OneToOneField(to='life.Event'),
        ),
        migrations.AddField(
            model_name='participant',
            name='registrations',
            field=models.ForeignKey(null=True, to='life.Registration'),
        ),
    ]
