# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0013_auto_20150215_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('addressee', models.CharField(max_length=100)),
                ('address_1', models.CharField(max_length=100)),
                ('address_2', models.CharField(max_length=100, blank=True, null=True)),
                ('address_3', models.CharField(max_length=100, blank=True, null=True)),
                ('town', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=100)),
                ('our_reference', models.CharField(max_length=100, blank=True, null=True)),
                ('your_reference', models.CharField(max_length=100, blank=True, null=True)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('letter_title', models.CharField(max_length=100)),
                ('addressee_is_organisation', models.BooleanField(default=False)),
                ('addressee_is_representative', models.BooleanField(default=False)),
                ('sender_name', models.CharField(max_length=100)),
                ('sender_title', models.CharField(max_length=100)),
                ('barcode', models.CharField(max_length=100)),
                ('additional_data', models.TextField(blank=True, null=True)),
                ('content_template', models.ForeignKey(to='letters.ContentTemplate')),
                ('letterhead', models.ForeignKey(to='letters.Letterhead')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='lettertext',
            name='content_template',
        ),
        migrations.RemoveField(
            model_name='lettertext',
            name='letterhead',
        ),
        migrations.DeleteModel(
            name='LetterText',
        ),
        migrations.RemoveField(
            model_name='lettervariable',
            name='variable_value',
        ),
        migrations.AddField(
            model_name='letterhead',
            name='bottom_margin',
            field=models.IntegerField(default=30, help_text='Distance in mm from bottom edge of page to bottom edge of body text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letterhead',
            name='left_margin',
            field=models.IntegerField(default=15, help_text='Distance in mm from left edge of page to left edge of body text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letterhead',
            name='right_margin',
            field=models.IntegerField(default=15, help_text='Distance in mm from right edge of page to right edge of body text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letterhead',
            name='top_margin',
            field=models.IntegerField(default=15, help_text='Distance in mm from top edge of page to top edge of body text'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contenttemplate',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contenttemplate',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='letterhead',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='letterhead',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='logo',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='logo',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
