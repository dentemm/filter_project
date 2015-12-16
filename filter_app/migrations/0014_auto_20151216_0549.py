# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0013_auto_20151215_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='slug',
            field=models.CharField(max_length=16, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(unique=True, max_length=16),
        ),
    ]
