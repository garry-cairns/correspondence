# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0004_letterhead_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letterhead',
            name='layout',
        ),
        migrations.AddField(
            model_name='letterhead',
            name='font',
            field=models.IntegerField(help_text='Choices are restricted to those available as standard in PDFs. This is essential to our archiving requirements.', default=2, choices=[(1, 'Courier'), (2, 'Helvetica'), (3, 'Times')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='letterhead',
            name='logo_x',
            field=models.IntegerField(help_text='Distance in mm from left edge of page to left edge of logo', default=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letterhead',
            name='logo_y',
            field=models.IntegerField(help_text='Distance in mm from top edge of page to top edge of logo', default=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letterhead',
            name='our_reference_x',
            field=models.IntegerField(help_text='Distance in mm from left edge of page to left edge of our reference', default=170),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letterhead',
            name='our_reference_y',
            field=models.IntegerField(help_text='Distance in mm from top edge of page to top edge of our reference', default=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letterhead',
            name='return_contacts',
            field=models.TextField(default='here'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letterhead',
            name='return_contacts_x',
            field=models.IntegerField(help_text='Distance in mm from left edge of page to left edge of return contacts', default=170),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letterhead',
            name='return_contacts_y',
            field=models.IntegerField(help_text='Distance in mm from top edge of page to top edge of return contacts', default=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letterhead',
            name='your_reference_x',
            field=models.IntegerField(help_text="Distance in mm from left edge of page to left edge of recipient's reference", default=170),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letterhead',
            name='your_reference_y',
            field=models.IntegerField(help_text="Distance in mm from top edge of page to top edge of recipient's reference", default=30),
            preserve_default=False,
        ),
    ]
