from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
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
            "detailsUrl": "static/places/moscow_legends.json"
        }
        features.append(points)

    contex = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, 'index.html', {'places_geojson': contex})


def show_place_id(request, place_id):
    obj = get_object_or_404(Place, pk=place_id)
    place = obj.title

    return HttpResponse(place)
