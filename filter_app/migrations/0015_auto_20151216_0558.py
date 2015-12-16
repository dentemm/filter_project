# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0014_auto_20151216_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='slug',
            field=models.CharField(default=b'tja', max_length=16),
        ),
    ]
