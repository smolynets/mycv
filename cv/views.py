from django.shortcuts import render

def one(request):
	return render(request, 'cv/one.html', {})

def two(request):
	return render(request, 'cv/two.html', {})
