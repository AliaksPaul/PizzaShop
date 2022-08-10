from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('error404/', views.page_not_found, name='error404'),
]
