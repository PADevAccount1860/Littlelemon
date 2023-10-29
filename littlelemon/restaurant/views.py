from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

