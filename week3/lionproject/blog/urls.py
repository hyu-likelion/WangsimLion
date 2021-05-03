from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('home/', views.home, name="home"),
    path('<str:id>', views.detail, name="detail"),
    path('newpost/', views.blogpost, name='newpost'),
    path('editpost/<str:id>', views.editpost, name='editpost'),
    path('delete/<str:id>', views.delete, name="delete"),

]