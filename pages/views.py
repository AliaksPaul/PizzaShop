from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer


class PizzaListView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return Response(template_name="pages/main.html")
