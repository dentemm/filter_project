# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chemistry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('concentration', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'chemistry',
                'verbose_name_plural': 'chemicals',
            },
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_code', models.CharField(unique=True, max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('pore_size', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'filter',
                'verbose_name_plural': 'filters',
            },
        ),
        migrations.CreateModel(
            name='FilterSwap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'Date')),
                ('who', models.CharField(max_length=32, null=True)),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': 'filter swap',
                'verbose_name_plural': 'filter swaps',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('chemistry', models.ManyToManyField(related_name='modules', to='filter_app.Chemistry')),
                ('current_filter', models.ForeignKey(related_name='+', to='filter_app.Filter')),
            ],
            options={
                'verbose_name': 'module',
                'verbose_name_plural': 'modules',
            },
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=8)),
                ('cleanroom', models.CharField(default=b'FAB1', max_length=16, null=True, choices=[(b'FAB1', b'FAB1'), (b'FAB2', b'FAB2')])),
            ],
            options={
                'ordering': ['cleanroom', 'name'],
                'verbose_name': 'tool',
                'verbose_name_plural': 'tools',
            },
        ),
        migrations.AddField(
            model_name='module',
            name='main_tool',
            field=models.ForeignKey(to='filter_app.Tool'),
        ),
        migrations.AddField(
            model_name='module',
            name='previous_filter',
            field=models.ForeignKey(related_name='+', to='filter_app.Filter', null=True),
        ),
        migrations.AddField(
            model_name='filterswap',
            name='module',
            field=models.ForeignKey(related_name='swaps', to='filter_app.Module'),
        ),
        migrations.AddField(
            model_name='filterswap',
            name='swapped_filter',
            field=models.ForeignKey(related_name='swaps', to='filter_app.Filter'),
        ),
    ]
