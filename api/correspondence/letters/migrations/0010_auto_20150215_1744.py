# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0009_auto_20150215_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lettertext',
            name='addressee_is_organisation',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lettertext',
            name='addressee_is_representative',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
