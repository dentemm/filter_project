# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='last_swap',
            field=models.DateField(null=True),
        ),
    ]
