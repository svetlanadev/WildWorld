from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views


urlpatterns = [
	url(r'^$', views.index, name = 'blog')
]

#urlpatterns = [
#	url(r'^$', views.home_page, name = 'blog')
#]

#urlpatterns = patterns('',
#	url(r'^$', 'views.index', name = 'index'))
