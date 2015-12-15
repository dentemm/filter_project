# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0005_module_extra_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='recommended_filter',
            field=models.ForeignKey(related_name='+', to='filter_app.Filter', null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='extra_info',
            field=models.TextField(null=True, blank=True),
        ),
    ]
