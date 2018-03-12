from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'experience/', views.experience, name='experience'),
	url(r'education/', views.education, name='education'),
	url(r'professional_skills/', views.professional_skills,
	 name='professional_skills'),
	url(r'technologies/', views.technologies, name='technologies'),
	url(r'personal_data/', views.personal_data, name='personal_data'),
]