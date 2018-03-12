from django.shortcuts import render

def home(request):
	return render(request, 'cv/home.html', {})

def experience(request):
	return render(request, 'cv/experience.html', {})

def education(request):
	return render(request, 'cv/education.html', {})

def professional_skills(request):
	return render(request, 'cv/professional_skills.html', {})

def technologies(request):
	return render(request, 'cv/technologies.html', {})

def personal_data(request):
	return render(request, 'cv/personal_data.html', {})
