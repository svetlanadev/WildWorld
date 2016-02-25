from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_lenth=128, unique=True)

	def __str__(self):
		return self.name

#	def __unicode__(self):
#		return self.name