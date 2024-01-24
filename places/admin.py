from django.contrib import admin
from .models import Place, Image


class PlaceAdmin(admin.ModelAdmin):
    pass
class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Place, PlaceAdmin)
admin.site.register(Image, ImageAdmin)
# Register your models here.
