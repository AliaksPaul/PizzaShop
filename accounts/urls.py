from django.urls import path
from . import views


urlpatterns = [
    # http://localhost:8000/registration/
    path('', views.RegistrationListView.as_view(), name='registration'),
    # http://localhost:8000/registration/profile/
    path('profile/', views.ProfileListView.as_view(), name='profile'),
    # http://localhost:8000/registration/email/
    path('email/', views.EmailListView.as_view(), name='email'),
]
