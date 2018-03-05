from django.shortcuts import render

def one(request):
	return render(request, 'cv/one.html', {})

