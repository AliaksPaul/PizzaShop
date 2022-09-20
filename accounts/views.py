from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .models import User 
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from .forms import UserRegistrationForm


class SignUpListView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return Response(template_name="accounts/registration.html")


class SignInListView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return Response(template_name="accounts/login.html")

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user) 
                    return redirect('main')
                return HttpResponse('Disabled account')
            return HttpResponse('Invalid login')
        return Response(template_name="accounts/login.html")


class ProfileListView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        return Response(template_name="registration/profile.html")


class EmailListView(generics.ListAPIView):
    queryset = User.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        self.objects = self.get_queryset()
        return Response({'emails' : self.objects}, template_name="accounts/email_layout.html")
