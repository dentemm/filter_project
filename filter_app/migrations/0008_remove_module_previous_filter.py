# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0007_auto_20151215_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='previous_filter',
        ),
    ]
