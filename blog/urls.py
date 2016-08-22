from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views 

app_name = "blog"
urlpatterns = [
	url(r'^$', views.index),
	url(r'^index', views.index, name='index'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^allposts/(.*)', views.allposts, name='allposts'),
	url(r'^post/(?P<post_id>[0-9]+)/$', views.post_detail, name = 'post_detail'),
	# url(r'^post/add/$', views.post_add, name='post_add'),
	url(r'^post/(?P<post_id>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^allcategory/(.*)', views.allcategory, name='allcategory'),
	url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='category'),
	url(r'^poems', views.poems, name='poems'),
	url(r'^poem/(?P<poem_id>[0-9]+)/$', views.poem, name='poem'),
	url(r'^poem/add/$', views.poem_add, name='poem_add'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='user_login'),
	# url(r'^restricted/', views.restricted, name='restricted'),
	url(r'^logout/', views.user_logout, name='logout'),
	url(r'^post/(?P<post_id>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
	# url(r'^category/add/', views.category_add, name='category_add'),

	url(r'^(?P<question_id>\d+)/results/$', views.results, name="results"),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name="vote"),
    url(r'^test', views.test, name='test')
]

#We recommend that you use hyphens (-) instead of underscores (_) in your URLs
 

