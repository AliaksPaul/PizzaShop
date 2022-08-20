from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User


def registration(request):
    """Function for registration"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            return render(request, 'account/registration_complete.html')
        return render(request, 'account/registration.html', {'user_form': user_form})
    user_form = UserRegistrationForm()
    return render(request, 'account/registration.html', {'user_form': user_form})

def email(request):
    return render(request, 'accounts/email_layout.html')

