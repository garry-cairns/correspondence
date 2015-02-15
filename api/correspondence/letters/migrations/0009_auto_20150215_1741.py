# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0008_auto_20150215_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lettertext',
            name='letter_title',
            field=models.CharField(max_length=100, default='Title'),
            preserve_default=False,
        ),
    ]
