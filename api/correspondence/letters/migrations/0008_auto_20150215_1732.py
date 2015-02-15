# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0007_auto_20150215_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='lettertext',
            name='addressee_is_organisation',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lettertext',
            name='addressee_is_representative',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lettertext',
            name='letter_title',
            field=models.CharField(blank=True, null=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lettertext',
            name='sender_name',
            field=models.CharField(default='Sender', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lettertext',
            name='sender_title',
            field=models.CharField(default='Letter sender', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contenttemplate',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contenttemplate',
            name='end_time',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contenttemplate',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lettertext',
            name='date_sent',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
