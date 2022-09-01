from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .models import CustomUser 
# from .forms import UserRegistrationForm


class RegistrationListView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return Response(template_name="registration/registration.html")


class ProfileListView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        return Response(template_name="registration/profile.html")


class EmailListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        self.objects = self.get_queryset()
        return Response({'emails' : self.objects}, template_name="accounts/email_layout.html")
