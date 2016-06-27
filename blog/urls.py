from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^index', views.index, name='index'),
	url(r'^sveta_contact', views.sveta_contact),
	url(r'^allposts/(.*)', views.allposts, name='allposts'),
	url(r'^post/(?P<post_id>[0-9]+)/$', views.post_detail, name = 'post_detail'),
	url(r'^post/add/$', views.post_add, name='post_add'),
	url(r'^post/(?P<post_id>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^allcategory/(.*)', views.allcategory, name='allcategory'),
	url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='category'),
	url(r'^poems', views.poems, name='poems'),
	url(r'^poem/(?P<poem_id>[0-9]+)/$', views.poem, name='poem'),

	url(r'^(?P<question_id>\d+)/results/$', views.results, name="results"),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name="vote"),
    url(r'^test', views.test, name='test')
]
 

