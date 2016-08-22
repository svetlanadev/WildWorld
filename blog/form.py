from django import forms
from django.contrib.auth.models import User
from .models import Post, Poems, UserProfile, Comment, Category

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','category', 'body',)

class PoemForm(forms.ModelForm):
	class Meta:
		model = Poems
		fields = ('title', 'body', 'author',)

#------ Create User Form
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('location', 'profile_picture',)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		exclude = ["post"]

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ('name',)