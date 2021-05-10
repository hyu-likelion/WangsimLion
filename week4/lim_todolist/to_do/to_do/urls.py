"""to_do URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
import model.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', model.views.home, name='home'),
    path('create/', model.views.create, name='create'),
    path('delete/<str:todos_id>/', model.views.delete, name='delete'),
    path('edit/<str:todos_id>/', model.views.edit, name='edit'),
    path('update/<str:todos_id>/', model.views.update, name='update'),
]
