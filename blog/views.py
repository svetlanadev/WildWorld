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
	return render(request, 'index.html', {'lamps' : posts, 'category_sequence' : categories_any_variable, 'allpoems' : poems_variable})

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


def poems(request, poem_num):
	poem = Poems.objects.get(id=poem_num)
	return render(request, 'poems.html', {'allpoems' : poem})


def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)



 