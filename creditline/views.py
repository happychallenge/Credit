from django.shortcuts import render

# Create your views here.
def index(request):
	template = 'creditline/index.html'
	context = {}
	return render(request, template, context)

def create(request):
	template = 'creditline/create.html'
	context = {}
	return render(request, template, context)

def detail(request, pk):
	template = 'creditline/create.html'
	context = {}
	return render(request, template, context)

def finish(request):
	template = 'creditline/finish.html'
	context = {}
	return render(request, template, context)