from django.db import models


class Place(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    description_short = models.TextField(verbose_name="Короткое описание", max_length=500, blank=True)
    description_long = models.TextField(verbose_name="Длинное описание", blank=True)
    lat = models.FloatField(verbose_name='Широта')
    lng = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title
