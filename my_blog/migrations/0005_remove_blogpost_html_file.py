# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0004_auto_20171125_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='html_file',
        ),
    ]
