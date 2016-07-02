from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
#from blog.models import TemplateView
from blog.models import Post, Category, Poems
from blog.form import PostForm, PoemForm
from django.shortcuts import redirect 

class MyStruct(object): 
		pass


# -----def index - Home page 
def index(request):
	post = Post.objects.order_by('-created')[:3]
	categ = Category.objects.all()
	poems_variable = Poems.objects.all()
	return render(request, 'index.html', {'posts' : post, 'categories' : categ, 'allpoems' : poems_variable})


# -----def allposts, def post_detail - This functions displays posts
def allposts(request, allpostsnum):
	post = Post.objects.order_by('-created')
	return render(request, 'allposts.html', {'posts' : post})


def post_detail(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	return render(request, 'post_detail.html', {'post' : post})


def post_add(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('blog.views.index')
	else:
		form = PostForm()
	return render(request, 'post_add.html', {'form' : form})


def post_edit(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			form.save()
			return redirect('blog.views.index')
	else:
		form = PostForm(instance=post)
	return render(request, 'post_add.html', {'form' : form})


# -----def allcategory, categoryDisplay - This functions displays Categories
def allcategory(request, allcateg_num):
	categories = Category.objects.all()
	return render(request, 'all_categories.html', {'categories' : categories})

def category(request, category_id):
	context_dict = {}
	try:
		category = Category.objects.get(id=category_id)
		context_dict['category_id'] = category.id
		posts = Post.objects.filter(category=category)
		context_dict['posts'] = posts
		context_dict['category'] = category
	except Category.DoesNotExist: 
		pass
	return render(request, 'category.html', context_dict)


# def categoryDisplay(request, categ_name):
# 	categoryItem = Category.objects.get(id=categ_name)
# 	return render(request, 'category_one.html', {'categoryItem' : categoryItem, 'posts': Post.objects.filter(category=categoryItem)})

# -----def poems, def poem - This functions displays poems
def poems(request):
	poems = Poems.objects.all()
	return render(request, 'poems.html', {'poems' : poems})

def poem(request, poem_id):
	poem = get_object_or_404(Poems, id=poem_id)
	return render(request, 'poem.html', {'poem' : poem})

def poem_add(request):
	# POST or GET method?
	if request.method == "POST":
		form = PoemForm(request.POST)
		if form.is_valid():
			form.save()
		# return redirect('some-view-name', foo='bar')	
		return redirect('blog.views.poems')
	else:
		form = PoemForm()
	return render(request, 'poem_add.html', {'form' : form})


# -----def sveta_contact - This function displays contacts
def contact(request):
	return render(request, 'contact.html',)



# ----  few functioons just for training 

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)

def test(request):
	latest_question_list = Post.objects.all()
	context = {'posts' : latest_question_list}
	return render(request, 'test.html', context)

