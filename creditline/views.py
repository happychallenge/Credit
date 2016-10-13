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

def history(request):
	template = 'creditline/history.html'
	context = {}
	return render(request, template, context)

def detail(request, pk):
	template = 'creditline/create.html'
	context = {}
	return render(request, template, context)

def change(request):
	template = 'creditline/change.html'
	context = {}
	return render(request, template, context)