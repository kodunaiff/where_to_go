from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableTabularInline, SortableAdminBase

from .models import Place, Image


class ImageInline(SortableTabularInline):
    model = Image
    readonly_fields = ['get_preview']
    fields = ['img', 'get_preview', 'number_pic']
    extra = 2

    def get_preview(self, obj):
        if not obj.img:
            return format_html('нет изображения')
        return format_html(f'<img src="{obj.img.url}" width=150 height=100>')

    get_preview.short_description = 'preview'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = (
        'title', 'description_short',
        'lat', 'lng',
    )

    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'number_pic', 'place', 'img']
