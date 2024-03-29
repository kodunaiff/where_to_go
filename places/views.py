from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Place


def show_places(request):
    places = Place.objects.all()

    places_geojson = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lng, place.lat]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': reverse('show_place_id', kwargs={'place_id': place.id})
                }
            }
            for place in places
        ]
    }
    context = {"places_geojson": places_geojson}
    return render(request, 'index.html', context)


def show_place_id(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related('places'), id=place_id)
    place_imgs = [image.img.url for image in place.places.all()]
    response_place = {
        'title': place.title,
        'imgs': place_imgs,
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat,
        }
    }

    return JsonResponse(response_place, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
