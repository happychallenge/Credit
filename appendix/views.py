from django.shortcuts import render

# 커멘트 추가 Comment
# Create your views here.
def index(request):
	template = 'appendix/index.html'
	context = {}
	return render(request, template, context)

def create(request):
	template = 'appendix/create.html'
	context = {}
	return render(request, template, context)

def history(request):
	template = 'appendix/history.html'
	context = {}
	return render(request, template, context)

def detail(request, pk):
	template = 'appendix/create.html'
	context = {}
	return render(request, template, context)

def change(request):
	template = 'appendix/change.html'
	context = {}
	return render(request, template, context)