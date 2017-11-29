from __future__ import unicode_literals
import os
from _datetime import datetime
from django.db import models

# for slug get_absolute_url
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

# delete md_file before delete/change model
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from unidecode import unidecode
from taggit.managers import TaggableManager

# Create your models here.

# upload_dir = 'content/BlogPost/%s/%s'
upload_dir = 'upload/%s/%s'


class BlogPost(models.Model):
    class Meta:
        ordering = ['-pub_date']  # ordered by pub_date descending

    def get_upload_md_name(self, filename):
        if self.pub_date:
            year = self.pub_date.year
        else:
            year = datetime.now().year
        upload_to = upload_dir % (year, self.title + '.md')
        return upload_to

    def get_html_name(self, filename):
        if self.pub_date:
            year = self.pub_date.year
        else:
            year = datetime.now().year
        upload_to = upload_dir % (year, filename)
        return upload_to

    CATEGORY_CHOICE = (
        ('about', 'About'),
        ('notes', 'Notes'),
        ('article', 'Article'),
        ('stem', 'STEM'),
        ('machine learning', 'Machine Learning'),
        ('deep learning', 'Deep Learning'),
        ('cpp', 'C++'),
        ('python', 'Python'),
        ('java', 'Java'),
    )

    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    md_file = models.FileField(upload_to=get_upload_md_name, blank=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    last_edit_date = models.DateTimeField('last edited', auto_now=True)
    slug = models.SlugField(max_length=200, blank=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICE)
    description = models.TextField(blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    @property
    def filename(self):
        if self.md_file:
            return os.path.basename(self.title)
        else:
            return 'no md_fild'

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        if not self.body and self.md_file:
            self.body = self.md_file.read()

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('my_blog.views.blogpost',
                       kwargs={'slug': self.slug, 'post_id': self.id})


@receiver(pre_delete, sender=BlogPost)
def blogpost_delete(instance, **kwargs):
    if instance.md_file:
        instance.md_file.delete(save=False)


class BlogPostImage(models.Model):
    def get_upload_img_name(self, filename):
        upload_to = upload_dir % ('images', filename)  # filename involves extension
        return upload_to

    blogpost = models.ForeignKey(BlogPost, related_name='images')
    image = models.ImageField(upload_to=get_upload_img_name)
