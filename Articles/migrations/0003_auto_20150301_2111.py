# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0002_auto_20150301_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='champion',
            field=models.ForeignKey(to='Articles.Champion'),
            preserve_default=True,
        ),
    ]
