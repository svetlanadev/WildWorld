from django import forms
from .models import Post, Poems

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','category', 'body',)

class PoemForm(forms.ModelForm):
	class Meta:
		model = Poems
		fields = ('title', 'body', 'author',)
