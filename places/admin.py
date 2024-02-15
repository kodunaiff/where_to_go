from adminsortable2.admin import SortableTabularInline, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(SortableTabularInline):
    model = Image
    readonly_fields = ['get_preview']
    fields = ['img', 'get_preview', 'number_pic']
    extra = 2

    def get_preview(self, obj):
        if not obj.img:
            return format_html('нет изображения')
        return format_html('<img src="{}" style="max-width:150px; max-height:100px;">', obj.img.url)

    get_preview.short_description = 'preview'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = (
        'id', 'title', 'short_description',
        'lat', 'lng',
    )

    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['place', 'number_pic', 'img']
    raw_id_fields = ['place']
