from django.urls import path

from .views import index, add_project

app_name = 'postings'

urlpatterns = [
    path('', index, name='index'),
    path('newproject/', add_project, name='add_project')
    ]