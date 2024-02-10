import logging
import sys
from time import sleep

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = "loads new data via link"

    def add_arguments(self, parser):
        parser.add_argument('-l', '--link', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            for url in options['link']:
                place, imgs_url = add_place(url)
                for url_number, img_url in enumerate(imgs_url, 1):
                    img_name = img_url.split('/')[-1]
                    img_num = url_number
                    get_img(place, img_url, img_num, img_name)

        except TypeError:
            logging.warning('Вы не передали ссылку на объект')
        except requests.exceptions.MissingSchema:
            logging.warning('Неверный тип ссылки')
        except requests.exceptions.HTTPError:
            logging.warning('Неккоректная ссылка')
        except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
            print('Отсутствие соединения, ожидание 10 сек...', file=sys.stderr)
            sleep(10)
        except Exception:
            logging.warning('Произошла ошибка')


def add_place(url):
    response = requests.get(url)
    response.raise_for_status()
    place = response.json()
    obj, created = Place.objects.get_or_create(
        title=place['title'],
        description_short=place['description_short'],
        description_long=place['description_long'],
        lat=place['coordinates']['lat'],
        lng=place['coordinates']['lng'],
    )
    return obj, place['imgs']


def get_img(place, img_url, img_num, img_name):
    response = requests.get(img_url)
    response.raise_for_status()
    Image.objects.create(
        number_pic=img_num,
        place=place,
        img=ContentFile(
            response.content,
            name=img_name
        )
    )
