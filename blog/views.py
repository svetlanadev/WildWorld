from django.shortcuts import render
from django.http import HttpResponse
import datetime
#from blog.models import TemplateView
from blog.models import Post, Category

class MyStruct(object):
		pass

def home_page(request):
    return HttpResponse('<html><title>Blog lists</title>Hello Blog <br> "You must be joking!" I can hear you say.</html>')


def index(request):
	posts = Post.objects.all()
	categories = Category.objects.all()
	return render(request, 'blog_index.html', {'articles' : posts, 'categories' : categories})


def sveta_contact(request):
	return render(request, 'sveta_contact.html',)

def all_categories(request):
	categories = Category.objects.all()
	return render(request, 'all_categories.html', {'categories' : categories})

def category_link(request):
	return render(request, 'blog_index.html', {'article' : post})


def post(request, post_num):
	post = Post.objects.get(id=post_num)
	# post = {'title' : 'myTitle', 'body' : 'my body'}
	return render(request, 'post.html', {'article' : post})





#   def index(request):
#	context_dict = {'title': "It's my blog", 'boldmessage': "I'm bold font from the context"}
#	return render(request, 'index.html', context_dict)

# Create your views here.
#home_page = None

#def home_page(request):
#	return HttpResponse('<html><title>To-Do lists</title>Hello Blog "You must be joking" I can hear you say.</html>')

#def index(request):
#	return HttpResponse('Rango says hello world!')
