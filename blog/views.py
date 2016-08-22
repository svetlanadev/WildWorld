from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post, Category, Poems, Comment
from blog.form import PostForm, PoemForm, UserForm, UserProfileForm, CommentForm, CategoryForm
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime


class MyStruct(object): 
		pass


def index(request):
	post = Post.objects.order_by('-created')[:3]
	categ = Category.objects.all()
	comment = Comment.objects.filter(post=post)
	poems_variable = Poems.objects.all()
	return render(request, 'index.html', {'posts' : post, 'categories' : categ, 'comments' : comment, 'allpoems' : poems_variable, 'media_base' : settings.MEDIA_URL })

# -----def allposts, def post_detail - This functions displays posts
def allposts(request, allpostsnum):
	post = Post.objects.order_by('-created')
	categ = Category.objects.all()
	return render(request, 'allposts.html', {'posts' : post, 'categories' : categ})


def post_detail(request, post_id): 
	post = get_object_or_404(Post, id=post_id)
	comment = Comment.objects.filter(post=post)
	categ = Category.objects.all()
	return render(request, 'post_detail.html', {'post' : post, 'comments' : comment, "form":CommentForm(), "user":request.user, 'categories' : categ, 'media_base' : settings.MEDIA_URL })






def post_edit(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			form.save()
			return redirect('/index/')
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
		return redirect('/poems/')
	else:
		form = PoemForm()
	return render(request, 'poem_add.html', {'form' : form})


# -----def sveta_contact - This function displays contacts
def contact(request):
	categ = Category.objects.all()
	return render(request, 'contact.html', {'categories' : categ})


# -----def  - This functions create users
def register(request):
    registered=False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save() 
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_picture' in request.FILES:
                profile_picture = request.FILES['profile_picture']
            profile.save()
            registered = True
        else:
            print (user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 
        'register.html',
  	    {'user_form' : user_form, 'profile_form' : profile_form, 'registered' : registered} )

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")				
    else:
        return render(request, 'login.html', {})

@login_required
def registered(request):
	return HttpResponse("You see it if you are registered")

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/index/')


# def category_add(request):
#     if request.method == "POST":
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#     else:
#         form = CategoryForm()
#     return render(request, "category_add.html", {'form' : form})

# def post_add(request):
#
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user.id
#             post.created = timezone.now()
#             post.save()
#             return redirect('/post_detail/', post_id=p.id)
#     else:
#         form = PostForm()
#     return render(request, "post_add.html", {"form" : form})


def add_comment_to_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("/index/", post_id=post.id)
    else:
        form = CommentForm()
    return render(request, "add_comment_to_post.html", {'form' : form})



# few functioons just for training

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def test(request):
    latest_question_list = Post.objects.all()
    context = {'posts' : latest_question_list}
    return render(request, 'test.html', context)
