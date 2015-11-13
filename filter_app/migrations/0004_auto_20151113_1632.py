# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0003_auto_20150925_1534'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tool',
            options={'ordering': ['cleanroom', 'name'], 'verbose_name': 'tool', 'verbose_name_plural': 'tools'},
        ),
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.CharField(unique=True, max_length=32, db_index=True),
        ),
    ]
