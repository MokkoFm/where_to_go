from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import Place
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


def index(request):
    moscow_legends = staticfiles_storage.url("places/moscow_legends.json")
    #roofs_24 = staticfiles_storage.url("places/roofs24.json")
    places = Place.objects.all()
    places_info = []

    for place in places:
        info = {
          "type": "FeatureCollection",
          "features": [
            {
              "type": "Feature",
              "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
              },
              "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": moscow_legends,
              }
            },
          ]
        }

        places_info.append(info)

    context = {"value": places_info}

    return render(request, 'index.html', context=context)


def post_detail(request, id):
    place = get_object_or_404(Place, id=id)
    response = HttpResponse()
    response.write(place.title)

    return response