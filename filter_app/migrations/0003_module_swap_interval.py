# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0002_module_last_swap'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='swap_interval',
            field=models.IntegerField(null=True),
        ),
    ]
