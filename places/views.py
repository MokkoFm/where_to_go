from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import Place, Image
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def index(request):
    moscow_legends = staticfiles_storage.url("places/moscow_legends.json")
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

    data = {
      "title": place.title,
      "imgs": [image.picture.url for image in place.images.all()],
      "description_short": place.description_short,
      "description_long": place.description_long,
      "coordinates": {
        "lng": place.lng,
        "lat": place.lat
      }
    }

    response = JsonResponse(data, safe=False, json_dumps_params={
                            'ensure_ascii': False, "indent": 2})

    return response
