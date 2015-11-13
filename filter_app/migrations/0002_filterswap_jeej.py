# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filterswap',
            name='jeej',
            field=models.OneToOneField(related_name='neej', default=1, to='filter_app.Module'),
            preserve_default=False,
        ),
    ]
