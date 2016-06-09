from django.shortcuts import render
from django.http import HttpResponse
import datetime
#from blog.models import TemplateView
from blog.models import Post, Category, Poems

class MyStruct(object):
		pass


def index(request):
	posts = Post.objects.all()
	categ = Category.objects.all()
	poems_variable = Poems.objects.all()
	return render(request, 'index.html', {'lamps' : posts, 'category_sequence' : categ, 'allpoems' : poems_variable})

def allposts(request, allposts_num):
	posts = Post.objects.all()
	return render(request, 'allposts.html', {'lamps' : posts})


def post(request, post_num):
	post = Post.objects.get(id=post_num)
	# post = {'title' : 'myTitle', 'body' : 'my body'}
	return render(request, 'post.html', {'p' : post})

def allcategory(request, allcateg_num):
	categ = Category.objects.all()
	return render(request, 'all_categories.html', {'category_sequence' : categ})

def categoryDisplay(request, categ_name):
	categoryItem = Category.objects.get(id=categ_name)
	return render(request, 'category_one.html', {'categoryItem' : categoryItem, 'lamps': Post.objects.filter(category=categoryItem)})


def poems(request, poem_num):
	poemses = Poems.objects.get(id=poem_num)
	return render(request, 'poems.html', {'allpoems' : poemses})


def o_nas(request):
	return render(request, 'o_nas.html')

def sveta_contact(request):
	return render(request, 'sveta_contact.html',)





# ----  few functioons just for training 

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)



 