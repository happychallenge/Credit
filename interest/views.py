from django.shortcuts import render

# Create your views here.
def index(request):
	template = 'interest/index.html'
	context = {}
	return render(request, template, context)

def history(request):
	template = 'interest/history.html'
	context = {}
	return render(request, template, context)

def create(request):
	template = 'interest/create.html'
	context = {}
	return render(request, template, context)

def result(request):
	template = 'interest/result.html'
	context = {}
	return render(request, template, context)

