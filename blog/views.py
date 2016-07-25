from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post, Category, Poems
from blog.form import PostForm, PoemForm, UserForm, UserProfileForm
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime


class MyStruct(object): 
		pass


# -----def index - Home page 
def index(request):
	post = Post.objects.order_by('-created')[:3]
	categ = Category.objects.all()
	poems_variable = Poems.objects.all()
	visits = int(request.COOKIES.get('visits',1))
	reset_last_visit_time = False
	return render(request, 'index.html', {'posts' : post, 'categories' : categ, 'allpoems' : poems_variable, 'media_base' : settings.MEDIA_URL })
 #    if 'last_visit' in request.COOKIES():
 #    	last_visit = request.COOKIES['last_visit']
 #    	last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S"))
 #        if (datetime.now() - last_visit_time).days > 0):
	#         visits = visits + 1
	#         reset_last_visit_time = True
	# else:
	# 	reset_last_visit_time = True
	# 	context_dict['visits'] = visits
	# 	response = render(request, 'index.html', context_dict)
 #    if reset_last_visit_time:
 #    	response.set.cookie('last_visit_time', datatime.now())
 #    	response.set.cookie('visits', visits)


# -----def allposts, def post_detail - This functions displays posts
def allposts(request, allpostsnum):
	post = Post.objects.order_by('-created')
	return render(request, 'allposts.html', {'posts' : post})


def post_detail(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	return render(request, 'post_detail.html', {'post' : post, 'media_base' : settings.MEDIA_URL })


def post_add(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/index/')

        #     # Profile image supplied? If so, we put it in the new UserProfile.
        # if 'image' in request.FILES:
        #     post.image = request.FILES['image']
        #     # Now we save the model instance!
        # 	post.save()
        #     # We can say registration was successful.
        #     registered = True			
	else:
		form = PostForm()
	return render(request, 'post_add.html', {'form' : form})



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
	return render(request, 'contact.html', {})


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

