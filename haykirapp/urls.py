from django.urls import path
from . import views

app_name = 'haykirapp'

urlpatterns = [
    path('',views.listhaykir,name='listhaykir'), # sacilingir/haykirapp
    path('addhaykir/',views.addhaykir,name='addhaykir'), # sacilingir/haykirapp/addhaykir
]
