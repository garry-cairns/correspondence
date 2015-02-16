# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0015_auto_20150216_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='addressee_is_representative',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
