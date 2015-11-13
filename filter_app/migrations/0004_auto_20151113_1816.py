# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0003_auto_20151113_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='current_filter',
            field=models.ForeignKey(related_name='+', default=1, to='filter_app.Filter'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='previous_filter',
            field=models.ForeignKey(related_name='+', to='filter_app.Filter', null=True),
        ),
        migrations.AlterField(
            model_name='filterswap',
            name='module',
            field=models.ForeignKey(related_name='+', to='filter_app.Module'),
        ),
    ]
