from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.menu_page, name='menu'),
]