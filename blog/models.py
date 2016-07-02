from django.db import models

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __str__(self):  
		return self.name

BLOG_ITEM_STATUS = (
	('0', 'Draft'),
	('1', 'Published'),
	('2', 'Not Published'),
)

class Post(models.Model):
	category = models.ForeignKey(Category)
#	author = models.ForeignKey(User)
	title = models.CharField(max_length=128)
	body = models.TextField()
	status = models.CharField(max_length=1, choices=BLOG_ITEM_STATUS, default='0')
	url = models.URLField(blank=True)
	# image = models.ImageField(upload_to='PostImage', blank=True)	
	views = models.IntegerField(default=0)
	# likes = models.IntegerField(default=0)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title 

class Poems(models.Model):
	title = models.CharField(max_length=50)
	body = models.TextField()
	author = models.CharField(max_length=80)

	def __str__(self):
		return self.title 



