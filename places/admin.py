from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    raw_id_fields = ["place"]


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["image_preview"]
    fields = ["picture", "place", "position", "image_preview"]

    def image_preview(self, instance):
        try:
            return format_html(
                "<img src='{url}' width='{width}' height='{height}'/>",
                url=instance.picture.url, width="auto", height='200px')
        except ValueError:
            return "Preview will be here"


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    inlines = [
        ImageInline,
    ]
