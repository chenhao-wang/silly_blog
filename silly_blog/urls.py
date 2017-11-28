"""silly_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import patterns, url, include
from my_blog.feeds import BlogPostFeed
from my_blog import views as blog_views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^(?P<page>\d*)/$', 'my_blog.views.home'),
    url(r'^$', blog_views.home, name='home'),
    url(r'^(?P<slug>[-\w\d]+),(?P<post_id>\d+)/$', blog_views.blogpost),
    url(r'^archives/$', blog_views.archives, name='archives'),
    url(r'^rss/$', BlogPostFeed()),
    url('^article/(?P<freshness>.*)/$', blog_views.article),

    url(r'^notes/$', blog_views.notes, name='notes'),
    url(r'^about/$', blog_views.about, name='about'),
    url(r'^notes/machine-learning/$', blog_views.machine_learning, name='machine_learning'),
    url(r'^notes/deep-learning/$', blog_views.deep_learning, name='deep_learning'),
    url(r'^notes/cpp/$', blog_views.cpp, name='cpp'),
    url(r'^notes/python/$', blog_views.python, name='python'),
    url(r'^notes/java/$', blog_views.java, name='java'),

    # admin
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
