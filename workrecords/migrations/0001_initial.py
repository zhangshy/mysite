# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('work_text', models.CharField(max_length=200)),
                ('rec_date', models.DateTimeField(verbose_name='date recorded', default=datetime.datetime(2015, 1, 17, 15, 10, 28, 903273, tzinfo=utc))),
                ('work_path', models.CharField(max_length=100)),
                ('remarks', models.CharField(null=True, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
