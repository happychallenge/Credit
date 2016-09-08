from django.shortcuts import render

# Create your views here.
def index(request):
	template = 'loan/index.html'
	context = {}
	return render(request, template, context)

def create1(request):
	template = 'loan/create1.html'
	context = {}
	return render(request, template, context)

def create2(request):
	template = 'loan/create2.html'
	context = {}
	return render(request, template, context)

def create3(request):
	template = 'loan/create3.html'
	context = {}
	return render(request, template, context)

def detail(request, pk):
	template = 'loan/detail.html'
	context = {}
	return render(request, template, context)

def finish(request):
	template = 'loan/finish.html'
	context = {}
	return render(request, template, context)