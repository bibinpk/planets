from django.contrib import admin

# Register your models here.
from destinations.models import countries, destinations, popular_places, popular_countries, slider

admin.site.register(countries)
admin.site.register(destinations)
admin.site.register(popular_places)
admin.site.register(popular_countries)
admin.site.register(slider)