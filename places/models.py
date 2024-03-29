from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250, unique=True)
    short_description = models.TextField(verbose_name="Короткое описание", blank=True)
    long_description = HTMLField(verbose_name="Длинное описание", blank=True)
    lat = models.FloatField(verbose_name='Широта')
    lng = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    number_pic = models.PositiveIntegerField(verbose_name='Номер картинки', default=0, db_index=True)
    place = models.ForeignKey('Place', verbose_name='Место', on_delete=models.CASCADE, related_name='places')
    img = models.ImageField(upload_to='media/', verbose_name='Картинка')

    def __str__(self):
        return f'{self.number_pic} {self.place}'

    class Meta:
        ordering = ['number_pic', 'place']
