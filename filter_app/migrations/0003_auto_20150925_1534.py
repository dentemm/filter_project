# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0002_filterswap_who'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filterswap',
            options={'ordering': ['-date'], 'verbose_name': 'filter swap', 'verbose_name_plural': 'filter swaps'},
        ),
        migrations.AddField(
            model_name='tool',
            name='cleanroom',
            field=models.CharField(default=b'FAB1', max_length=16, null=True, choices=[(b'FAB1', b'FAB1'), (b'FAB2', b'FAB2')]),
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(unique=True, max_length=8),
        ),
    ]
