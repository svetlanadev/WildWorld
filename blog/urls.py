from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^index/', views.index, name='index'),
	url(r'^o_nas', views.o_nas),
	url(r'^sveta_contact', views.sveta_contact),
	url(r'^allposts/(.*)', views.allposts, name='allposts'),
	url(r'^post/([0-9]+)$', views.post, name = 'post_num'),
	url(r'^allcategory/(.*)', views.allcategory, name='allcategory'),
	url(r'^category/(.*)', views.categoryDisplay),
	url(r'^poems', views.poems, name='poems'),
	url(r'^(?P<question_id>\d+)/results/$', views.results, name="results"),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name="vote"),
    url(r'^test', views.test, name='test')
]

  
#urlpatterns = [
#	url(r'^$', views.home_page, name = 'blog')
#]

#urlpatterns = patterns('',
#	url(r'^$', 'views.index', name = 'index'))
 	# url(r'^allcategory/category/(.*)', views.categoryDisplay),