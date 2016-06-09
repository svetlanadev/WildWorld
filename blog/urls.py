from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^o_nas', views.o_nas),
	url(r'^sveta_contact', views.sveta_contact),
	url(r'^post/([0-9]+)$', views.post, name = 'post_num'),
	url(r'^category/(.*)', views.categoryDisplay),
	url(r'^poems/([0-9]+)$', views.poems),
	url(r'^(?P<question_id>\d+)/results/$', views.results, name="results"),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name="vote"),
]

 
#urlpatterns = [
#	url(r'^$', views.home_page, name = 'blog')
#]

#urlpatterns = patterns('',
#	url(r'^$', 'views.index', name = 'index'))
