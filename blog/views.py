from django.shortcuts import render
from django.http import HttpResponse
import datetime
#from blog.models import TemplateView
from blog.models import Post, Category, Poems

class MyStruct(object):
		pass

def home_page(request):
    return HttpResponse('<html><title>Blog lists</title>Hello Blog <br> "You must be joking!" I can hear you say.</html>')


def index(request):
	posts = Post.objects.all()
	categories_any_variable = Category.objects.all()
	poems_variable = Poems.objects.all()
	return render(request, 'blog_index.html', {'lamps' : posts, 'category_sequence' : categories_any_variable, 'allpoems' : poems_variable})

def o_nas(request):
	return render(request, 'o_nas.html')

def sveta_contact(request):
	return render(request, 'sveta_contact.html',)


def post(request, post_num):
	post = Post.objects.get(id=post_num)
	# post = {'title' : 'myTitle', 'body' : 'my body'}
	return render(request, 'post.html', {'banana' : post})


def categoryDisplay(request, categ_name):
	categoryItem = Category.objects.get(id=categ_name)
	return render(request, 'category_one.html', {'categoryItem' : categoryItem, 'lamps': Post.objects.filter(category=categoryItem)})


def poemses(request, poem_num):
	poem = Poems.objects.get(id=poem_num)
	return render(request, 'poems.html', {'mandarina' : poem})

# def category_link(request, cat_name):
# 	category_name = Category.objects.get(name=cat_name)
# 	posts = Post.objects.filter(category_link=category_name)
# 	return render(request, 'blog_index.html', {'allposts' : posts})



#   def index(request):
#	context_dict = {'title': "It's my blog", 'boldmessage': "I'm bold font from the context"}
#	return render(request, 'index.html', context_dict)

# Create your views here.
#home_page = None

#def home_page(request):
#	return HttpResponse('<html><title>To-Do lists</title>Hello Blog "You must be joking" I can hear you say.</html>')

#def index(request):
#	return HttpResponse('Rango says hello world!')
