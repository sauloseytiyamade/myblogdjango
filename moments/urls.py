from django.urls import path
from .views import moments_list

urlpatterns = [
    path('', moments_list.as_view(), name='home'),
]