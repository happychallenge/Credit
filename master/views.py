from django.shortcuts import render

# Bank
def bankindex(request):
	template = 'master/bankindex.html'
	context = {}
	return render(request, template, context)

def bankcreate(request):
	template = 'master/bankcreate.html'
	context = {}
	return render(request, template, context)

def bankdetail(request, pk):
	template = 'master/bankcreate.html'
	context = {}
	return render(request, template, context)

# Credit
def creditgradeindex(request):
	template = 'master/creditgradeindex.html'
	context = {}
	return render(request, template, context)

def creditgradecreate(request):
	template = 'master/creditgradecreate.html'
	context = {}
	return render(request, template, context)

def exchangerate(request):
	template = 'master/exchangerate.html'
	context = {}
	return render(request, template, context)
