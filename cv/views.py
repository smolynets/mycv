from django.shortcuts import render

def one(request):
	return render(request, 'cv/one.html', {})

def two(request):
	return render(request, 'cv/two.html', {})

def three(request):
	return render(request, 'cv/three.html', {})

def four(request):
	return render(request, 'cv/four.html', {})

def five(request):
	return render(request, 'cv/five.html', {})

def six(request):
	return render(request, 'cv/six.html', {})
