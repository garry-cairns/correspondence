# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0002_lettertext_additional_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='letterhead',
            name='logo',
        ),
    ]
