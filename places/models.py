from django.db import models


class Place(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    description_short = models.TextField(verbose_name="Короткое описание", max_length=500, blank=True)
    description_long = models.TextField(verbose_name="Длинное описание", blank=True)
    lat = models.FloatField(verbose_name='Широта')
    lng = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    number_pic = models.IntegerField(verbose_name='Номер картинки', null=True, blank=True)
    place = models.ForeignKey('Place', verbose_name='Место', on_delete=models.CASCADE, related_name='places')
    img = models.ImageField(verbose_name='Картинка', null=True, blank=True)


    def __str__(self):
        return f'{self.number_pic} {self.place}'

    class Meta:
        ordering = ['place', 'number_pic']

