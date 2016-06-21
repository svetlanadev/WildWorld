from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
#from blog.models import TemplateView
from blog.models import Post, Category, Poems

class MyStruct(object):
		pass

 
def index(request):
	post = Post.objects.order_by('-created')[:2]
	categ = Category.objects.all()
	poems_variable = Poems.objects.all()
	return render(request, 'index.html', {'posts' : post, 'category_sequence' : categ, 'allpoems' : poems_variable})


def allposts(request, allpostsnum):
	post = Post.objects.order_by('-created')
	return render(request, 'allposts.html', {'posts' : post})

# def allposts(request, allposts_num):
# 	post = Post.objects.order_by('-created')
# 	return render(request, 'allposts.html', {'posts' : post})


# def post(request, pk):
# 	post = Post.objects.get(id=pk)
# 	context = {'posts' : post}
# 	return render(request, 'post.html', context)



def post_detail(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	return render(request, 'post_detail.html', {'post' : post})

def allcategory(request, allcateg_num):
	categ = Category.objects.all()
	return render(request, 'all_categories.html', {'category_sequence' : categ})

def categoryDisplay(request, categ_name):
	categoryItem = Category.objects.get(id=categ_name)
	return render(request, 'category_one.html', {'categoryItem' : categoryItem, 'posts': Post.objects.filter(category=categoryItem)})


def poems(request):
	return render(request, 'poems.html')


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

def test(request):
	latest_question_list = Post.objects.all().order_by('-date')[:5]
	context = {'posts' : latest_question_list}
	return render(request, 'test.html', context)

 