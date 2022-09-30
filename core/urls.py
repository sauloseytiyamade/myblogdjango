"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from moments import urls as moments_urls
from about import urls as about_urls
from projects import urls as projects_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(moments_urls)),
    path('sobre', include(about_urls)),
    path('projects', include(projects_url)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
