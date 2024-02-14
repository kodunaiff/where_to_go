from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Place


def show_places(request):
    places = Place.objects.all()
    features = []
    for place in places:
        points = {}
        points['type'] = 'Feature'
        points['geometry'] = {
            "type": "Point",
            "coordinates": [place.lng, place.lat]
        }
        points['properties'] = {
            "title": place.title,
            "placeId": "moscow_legends",
            "detailsUrl": reverse("show_place_id", kwargs={"place_id": place.id})
        }
        features.append(points)

    contex = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, 'index.html', {'places_geojson': contex})


def show_place_id(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_imgs = [image.img.url for image in place.places.all()]
    response_place = {
        'title': place.title,
        'imgs': place_imgs,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat,
        }
    }

    return JsonResponse(response_place, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
