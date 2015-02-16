# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0014_auto_20150216_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='addressee',
        ),
        migrations.RemoveField(
            model_name='letter',
            name='addressee_is_organisation',
        ),
        migrations.AddField(
            model_name='letter',
            name='addressee_first_name',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='letter',
            name='addressee_organisation',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='letter',
            name='addressee_second_name',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='letter',
            name='addressee_title',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='letter',
            name='addressee_is_representative',
            field=models.BooleanField(),
            preserve_default=True,
        ),
    ]
