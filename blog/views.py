from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#home_page = None

#def home_page(request):
#	return HttpResponse('<html><title>To-Do lists</title>Hello Blog "You must be joking" I can hear you say.</html>')

def index(request):
	context_dict = {'title': "It's my blog", 'boldmessage': "I'm bold font from the context"}
	return render(request, 'index.html', context_dict)

#def index(request):
#	return HttpResponse('Rango says hello world!')
