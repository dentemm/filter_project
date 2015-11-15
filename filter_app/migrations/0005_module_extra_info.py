# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0004_remove_module_last_swap'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='extra_info',
            field=models.TextField(null=True),
        ),
    ]
