# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0003_auto_20150116_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='letterhead',
            name='logo',
            field=models.ForeignKey(to='letters.Logo', default=1),
            preserve_default=False,
        ),
    ]
