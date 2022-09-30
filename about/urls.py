from django.urls import path
from .views import about_list

urlpatterns = [
    path('', about_list.as_view(), name='about'),
]