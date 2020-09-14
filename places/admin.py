from django.contrib import admin
from .models import Place
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ["place"]


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
