# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0003_module_swap_interval'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='last_swap',
        ),
    ]
