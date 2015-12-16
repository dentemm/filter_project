# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0012_module_recommended_filter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chemistry',
            options={'ordering': ['name'], 'verbose_name': 'chemistry', 'verbose_name_plural': 'chemicals'},
        ),
        migrations.AlterModelOptions(
            name='filter',
            options={'ordering': ['manufacturer', 'product_code'], 'verbose_name': 'filter', 'verbose_name_plural': 'filters'},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['main_tool', 'name'], 'verbose_name': 'module', 'verbose_name_plural': 'modules'},
        ),
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='module',
            name='swap_interval',
            field=models.IntegerField(default=3, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='module',
            unique_together=set([('name', 'main_tool')]),
        ),
    ]
