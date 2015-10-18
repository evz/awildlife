# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='contact_info',
            field=models.ForeignKey(to='life.ContactInfo', null=True),
        ),
    ]
