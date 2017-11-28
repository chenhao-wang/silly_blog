# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0003_auto_20171125_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(max_length=30, choices=[('about', 'About'), ('notes', 'Notes'), ('article', 'Article'), ('stem', 'STEM'), ('machine learning', 'Machine Learning'), ('deep learning', 'Deep Learning'), ('cpp', 'C++'), ('python', 'Python'), ('java', 'Java')]),
        ),
    ]
