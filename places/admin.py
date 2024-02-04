from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview']
    fields = ['img', 'get_preview', 'number_pic']

    def get_preview(self, obj):
        return format_html(f'<img src="{obj.img.url}" width=150 height=100>')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description_short',
        'lat', 'lng',
    )

    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
