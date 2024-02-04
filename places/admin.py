from django.contrib import admin
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description_short',
        'lat', 'lng',
    )
    inlines = [
        ImageInline
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
