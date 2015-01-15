# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lettertext',
            name='additional_data',
            field=models.TextField(default='t'),
            preserve_default=False,
        ),
    ]
