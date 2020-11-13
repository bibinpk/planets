from django.shortcuts import render

# Create your views here.
from destinations.models import countries, popular_countries, slider, popular_places, destinations


def index(request):
    pop_dest = popular_places.objects.all().order_by('dest_id').reverse()
    pop = popular_countries.objects.all().order_by('cou_id').reverse()
    slide = slider.objects.all().order_by('slide_id').reverse()
    return render(request, 'index.html', {'pops': pop, 'slides': slide, 'pop_dests': pop_dest})


def destinationss(request, cou_name):
    cout = countries.objects.all()
    cou = countries.objects.get(name=cou_name)
    dest = destinations.objects.filter(country=cou)
    return render(request, 'travel_destination.html', {'couts': cout, 'dests': dest, 'conts': cou})


def destination(request, dest):
    de_dest = destinations.objects.get(name=dest)
    return render(request, 'destination_details.html', {'de_dests': de_dest})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
