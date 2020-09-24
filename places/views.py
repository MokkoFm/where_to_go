from django.shortcuts import render
from .models import Place
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse


def index(request):
    places = Place.objects.all()
    features_of_places = []

    for place in places:
        place_feature = {
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
                "detailsUrl": reverse("place_detail", args=[place.id]),
              }
            },
          ]
        }

        features_of_places.append(place_feature)

    context = {"value": features_of_places}

    return render(request, 'index.html', context=context)


def post_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    place_details = {
      "title": place.title,
      "imgs": [image.picture.url for image in place.images.all()],
      "description_short": place.description_short,
      "description_long": place.description_long,
      "coordinates": {
        "lng": place.lng,
        "lat": place.lat
      }
    }

    response = JsonResponse(place_details, safe=False, json_dumps_params={
                            'ensure_ascii': False, "indent": 2})

    return response
