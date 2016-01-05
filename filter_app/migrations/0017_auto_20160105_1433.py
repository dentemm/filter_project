# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0016_auto_20151222_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='number_of_filters',
            field=models.PositiveIntegerField(default=1, verbose_name=b'Number of filters'),
        ),
        migrations.AlterField(
            model_name='filterswap',
            name='comment',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.RemoveField(
            model_name='module',
            name='chemistry',
        ),
        migrations.AddField(
            model_name='module',
            name='chemistry',
            field=models.ManyToManyField(related_name='modules', to='filter_app.Chemistry'),
        ),
    ]
