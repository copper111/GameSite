# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('Articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='champion',
            field=models.CharField(max_length=300),
            preserve_default=True,
        ),
    ]
