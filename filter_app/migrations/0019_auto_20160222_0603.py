# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0018_filter_is_stock_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filter',
            options={'ordering': ['product_code'], 'verbose_name': 'filter', 'verbose_name_plural': 'filters'},
        ),
        migrations.AddField(
            model_name='filter',
            name='extra_info',
            field=models.TextField(null=True, verbose_name=b'Additional information', blank=True),
        ),
    ]
