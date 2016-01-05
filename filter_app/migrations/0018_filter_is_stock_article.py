# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0017_auto_20160105_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='is_stock_article',
            field=models.BooleanField(default=False),
        ),
    ]
