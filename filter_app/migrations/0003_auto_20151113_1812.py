# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0002_filterswap_jeej'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filterswap',
            name='jeej',
        ),
        migrations.RemoveField(
            model_name='module',
            name='current_filter',
        ),
        migrations.RemoveField(
            model_name='module',
            name='previous_filter',
        ),
    ]
