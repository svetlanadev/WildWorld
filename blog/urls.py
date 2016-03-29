from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views


urlpatterns = [
	url(r'^$', views.index, name = 'blog'),
	url(r'^sveta_contact', views.sveta_contact),
	url(r'^all_categories', views.all_categories),
#	url(r'^all_categories/(?P<category_num>[0-9]+)$', views.all_categories, name = 'category_num'),
	url(r'^post/(?P<post_num>[0-9]+)$', views.post, name = 'post_num'),
	url(r'^category', views.category_link),
]

#urlpatterns = [
#	url(r'^$', views.home_page, name = 'blog')
#]

#urlpatterns = patterns('',
#	url(r'^$', 'views.index', name = 'index'))

#urlpatterns = patterns('',
#	url(r'^$', 'post.html.index', name = 'index'))