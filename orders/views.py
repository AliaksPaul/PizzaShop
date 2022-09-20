from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

class CartListView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        return Response(template_name="registration/profile.html")

class OrdersListView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        return Response(template_name="orders/order_place.html")