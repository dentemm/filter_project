# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0009_module_previous_filter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='previous_filter',
        ),
        migrations.RemoveField(
            model_name='module',
            name='recommended_filter',
        ),
    ]
