# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0006_auto_20150208_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lettertext',
            old_name='address_4',
            new_name='town',
        ),
        migrations.RenameField(
            model_name='lettervariable',
            old_name='letter_variable',
            new_name='variable_name',
        ),
        migrations.RemoveField(
            model_name='contenttemplate',
            name='letterhead',
        ),
        migrations.RemoveField(
            model_name='lettertext',
            name='text',
        ),
        migrations.AddField(
            model_name='lettertext',
            name='letterhead',
            field=models.ForeignKey(default=1, to='letters.Letterhead'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lettervariable',
            name='variable_value',
            field=models.CharField(blank=True, null=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lettertext',
            name='additional_data',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lettertext',
            name='address_2',
            field=models.CharField(blank=True, null=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lettertext',
            name='address_3',
            field=models.CharField(blank=True, null=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lettertext',
            name='barcode',
            field=models.CharField(blank=True, null=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lettertext',
            name='our_reference',
            field=models.CharField(blank=True, null=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lettertext',
            name='your_reference',
            field=models.CharField(blank=True, null=True, max_length=100),
            preserve_default=True,
        ),
    ]
