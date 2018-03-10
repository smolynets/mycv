from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.one, name='one'),
	url(r'two/', views.two, name='two'),
	url(r'three/', views.three, name='three'),
	url(r'four/', views.four, name='four'),
	url(r'five/', views.five, name='five'),
	url(r'six/', views.six, name='six'),
]