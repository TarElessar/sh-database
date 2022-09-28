from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('excel/', views.read_excel, name='read_excel'),
]