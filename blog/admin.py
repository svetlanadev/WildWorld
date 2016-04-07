from django.contrib import admin
from models import Category
from models import Post
from models import Poems

# Register your models here.



class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'status']
	date_hierarchy = 'updated'
	ordering = ['title']
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


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Poems)