from django.core.management.base import BaseCommand
from places.models import Place
import requests
from django.core.files.base import ContentFile
from places.models import Image


class Command(BaseCommand):
    help = 'Upload place to a map'

    def add_arguments(self, parser):
        parser.add_argument("url", type=str)

    def handle(self, *args, **options):
        url = options.get("url")
        response = requests.get(url, allow_redirects=False)
        response.raise_for_status()
        place_data = response.json()

        place, created = Place.objects.get_or_create(
            title=place_data["title"], defaults={
                'description_short': place_data["description_short"],
                'description_long': place_data["description_long"],
                'lng': place_data["coordinates"]["lng"],
                'lat': place_data["coordinates"]["lat"]
            }
        )

        for img_number, img in enumerate(place_data["imgs"], start=1):
            response = requests.get(img, allow_redirects=False)
            response.raise_for_status()
            content = ContentFile(response.content)
            filename = img.split('/')[-1]
            new_image = Image()
            new_image.picture.save(filename, content, save=True)
            new_image.place = place
            new_image.position = img_number
            new_image.save()
