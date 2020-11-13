from django.urls import path

from destinations.views import index, destinations, destinationss, destination, contact, about

urlpatterns = [
    path('', index),
    path('destinations/<str:cou_name>/', destinationss),
    path('destination/<str:dest>/', destination),
    path('contact/', contact),
    path('about/', about)
]