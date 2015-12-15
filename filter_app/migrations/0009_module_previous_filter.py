# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0008_remove_module_previous_filter'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='previous_filter',
            field=models.ForeignKey(related_name='+', blank=True, to='filter_app.Filter', null=True),
        ),
    ]
