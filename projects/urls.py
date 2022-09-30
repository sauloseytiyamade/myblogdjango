from django.urls import path
from .views import projects_list

urlpatterns = [
    path('', projects_list.as_view(), name='projects'),
]