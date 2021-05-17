from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:id>', views.post, name='post'),
    path('', views.projects_index, name='projects_index'),
] 