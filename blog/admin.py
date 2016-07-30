from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Category, Post, Poems, UserProfile

# Register your models here.

class PostAdminForm(forms.ModelForm):

    body = forms.CharField(widget=CKEditorWidget())
    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'



class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'created', 'status']
	date_hierarchy = 'updated'
	ordering = ['created']
	actions = ['make_published', 'make_draft', 'make_not_published']

	def make_draft(self, request, queryset):
		queryset.update(status='0')
	make_draft.short_description = 'Mark selected stories as draft'

	def make_published(self, request, queryset):
		rows_updated = queryset.update(status='p')
		if rows_updated == 1:
			message_bit = '1 story was'
		else:
			message_bit = '%s stories were' % rows_updated
		self.message_user(request, '%s successfully marked as published.' % message_bit)
	make_published.short_description = "Mark selected stories as published"
	form = PostAdminForm


admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Post, PostAdmin)
# admin.site.register(Poems)
