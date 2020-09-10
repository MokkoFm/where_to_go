from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage


def index(request):
    moscow_legends = staticfiles_storage.url("places/moscow_legends.json")
    roofs_24 = staticfiles_storage.url("places/roofs24.json")

    context = {"value": {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.62, 55.793676]
          },
          "properties": {
            "title": "«Легенды Москвы",
            "placeId": "moscow_legends",
            "detailsUrl": moscow_legends,
          }
        },
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.64, 55.753676]
          },
          "properties": {
            "title": "Крыши24.рф",
            "placeId": "roofs24",
            "detailsUrl": roofs_24,
          }
        }
      ]
    }}
    return render(request, 'index.html', context=context)
