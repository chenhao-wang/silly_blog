from django import template
from my_blog.models import BlogPost

register = template.Library()


@register.simple_tag
def get_related(post):
    posts = BlogPost.objects.filter(
        tags__in=post.tags.all()
    ).filter(
        published=True
    ).exclude(
        pk=post.id
    ).distinct()[:3]

    return posts


@register.filter
def stripleadingzero(string):
    return string.lstrip('0')
