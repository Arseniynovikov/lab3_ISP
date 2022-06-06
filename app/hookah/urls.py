from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('menu', include('menu.urls')),
    path('nohome', views.nohome_page, name='nohome')
]
