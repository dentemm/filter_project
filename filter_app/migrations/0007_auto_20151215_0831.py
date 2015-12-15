# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0006_auto_20151215_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='current_filter',
            field=models.ForeignKey(related_name='+', blank=True, to='filter_app.Filter', null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='previous_filter',
            field=models.ForeignKey(related_name='+', blank=True, to='filter_app.Filter', null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='recommended_filter',
            field=models.ForeignKey(related_name='+', blank=True, to='filter_app.Filter', null=True),
        ),
    ]
