# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import my_blog.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField(blank=True)),
                ('md_file', models.FileField(blank=True, upload_to=my_blog.models.BlogPost.get_upload_md_name)),
                ('pub_date', models.DateTimeField(verbose_name='date published', auto_now_add=True)),
                ('last_edit_date', models.DateTimeField(verbose_name='last edited', auto_now=True)),
                ('slug', models.SlugField(max_length=200, blank=True)),
                ('html_file', models.FileField(blank=True, upload_to=my_blog.models.BlogPost.get_html_name)),
                ('category', models.CharField(max_length=30, choices=[('programming', 'Programming'), ('acg', 'Anime & Manga & Novel $ Game'), ('nc', 'No Category')])),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='BlogPostImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to=my_blog.models.BlogPostImage.get_upload_img_name)),
                ('blogpost', models.ForeignKey(related_name='images', to='my_blog.BlogPost')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='previous',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=taggit.managers.TaggableManager(verbose_name='Tags', help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag'),
        ),
    ]
