# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0015_auto_20151216_0558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='chemistry',
        ),
        migrations.AddField(
            model_name='module',
            name='chemistry',
            field=models.ForeignKey(related_name='modules', to='filter_app.Chemistry', null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='swap_interval',
            field=models.IntegerField(default=24, null=True, verbose_name=b'Swap interval (# months)'),
        ),
    ]
