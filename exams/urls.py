from django.urls import path
from . import views

app_name = exams

urlpatterns = [path('', views.index, name = 'index'), 
               
               ]