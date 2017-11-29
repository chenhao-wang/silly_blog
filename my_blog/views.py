from collections import defaultdict
from math import ceil
from os.path import join

from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404

from .models import BlogPost


# home page contains latest update in all topics except 'about' and 'notes' pages
def home(request, page=''):
    args = {'blogposts': BlogPost.objects.exclude(title__in=("about", "notes"))}
    max_page = ceil(len(args['blogposts']) / 3)
    if page and int(page) < 2:  # /0, /1 -> /
        return redirect("/")
    else:
        page = int(page) if (page and int(page) > 0) else 1
        args['page'] = page
        args['prev_page'] = page + 1 if page < max_page else None
        args['newer_page'] = page - 1 if page > 1 else None
        # as template slice filter, syntax: list|slice:"start:end"
        args['sl'] = str(3 * (page - 1)) + ':' + str(3 * (page - 1) + 3)
        return render(request, 'my_blog/index.html', args)


def blogpost(request, slug, post_id):
    request.encoding = 'utf-8'
    args = {'blogpost': get_object_or_404(BlogPost, pk=post_id)}
    return render(request, 'my_blog/blogpost.html', args)


# archives page contains categories including 'article' and 'stem'
def archives(request):
    args = dict()
    blogposts = BlogPost.objects.filter(category__in=("article", "stem"))

    def get_sorted_posts(category):
        posts_by_year = defaultdict(list)
        posts_of_a_category = blogposts.filter(category=category)  # already sorted by pub_date
        for post in posts_of_a_category:
            year = post.pub_date.year
            posts_by_year[year].append(post)  # {'2013':post_list, '2014':post_list}
        posts_by_year = sorted(posts_by_year.items(), reverse=True)  # [('2014',post_list), ('2013',post_list)]
        return posts_by_year

    args['data'] = [
        ('article', get_sorted_posts(category="article")),
        ('stem', get_sorted_posts(category="stem")),
    ]

    return render(request, 'my_blog/archives.html', args)


# about and notes page are single showed for redirecting
def about(request):
    the_about_post = get_object_or_404(BlogPost, category="about")
    args = {"about": the_about_post}
    return render(request, 'my_blog/about.html', args)


def notes(request):
    the_notes_post = get_object_or_404(BlogPost, category="notes")
    args = {"notes": the_notes_post}
    return render(request, 'my_blog/notes.html', args)


def notes_base(request, category):
    args = dict()
    blogposts = BlogPost.objects.filter(category=category)

    def get_sorted_posts():
        posts_by_year = defaultdict(list)
        for post in blogposts:
            year = post.pub_date.year
            posts_by_year[year].append(post)  # {'2013':post_list, '2014':post_list}
        posts_by_year = sorted(posts_by_year.items(), reverse=True)  # [('2014',post_list), ('2013',post_list)]
        return posts_by_year

    args['data'] = [
        (category, get_sorted_posts()),
    ]
    return render(request, 'my_blog/archives.html', args)


def machine_learning(request):
    return notes_base(request, "machine learning")


def deep_learning(request):
    return notes_base(request, "deep learning")


def cpp(request):
    return notes_base(request, "cpp")


def python(request):
    return notes_base(request, "python")


def java(request):
    return notes_base(request, "java")


def article(request, freshness):
    """ redirect to article accroding to freshness, latest->oldest:freshness=1->N """
    if freshness.isdigit():
        try:
            article_url = BlogPost.objects.all()[int(freshness) - 1].get_absolute_url()
            return redirect(article_url)
        except IndexError:
            raise Http404
        except AssertionError:  # freshness=0
            raise Http404
    else:
        return redirect('/')
