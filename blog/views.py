from django.shortcuts import render
from django.http import HttpResponse
import datetime

class MyStruct(object):
		pass

def home_page(request):
    return HttpResponse('<html><title>Blog lists</title>Hello Blog <br> "You must be joking!" I can hear you say.</html>')


def index(request):
	c = MyStruct()
	c.company = 'Cool Star'
	c.title = 'Cool Star Blog'
	c.author_name = 'Jhon Smith'
	c.pub_date = datetime.datetime.now()
	c.article_list = [{'title':'Title1', 'text':'Text1'},
		{'title':'Title2', 'text':'Text2'},
		{'title':'Title3', 'text':'Text3'}]
	return render(request, 'blog_index.html', c.__dict__)



#def index(request):
#	context_dict = {'title': "It's my blog", 'boldmessage': "I'm bold font from the context"}
#	return render(request, 'index.html', context_dict)

# Create your views here.
#home_page = None

#def home_page(request):
#	return HttpResponse('<html><title>To-Do lists</title>Hello Blog "You must be joking" I can hear you say.</html>')

#def index(request):
#	return HttpResponse('Rango says hello world!')
