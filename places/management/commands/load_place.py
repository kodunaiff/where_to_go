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
                place, img_urls, created = add_place(url)
                if not created:
                    logging.warning('данная локация уже в базе')
                    continue

                for url_number, img_url in enumerate(img_urls, 1):
                    img_name = img_url.split('/')[-1]
                    img_num = url_number
                    fetch_img(place, img_url, img_num, img_name)

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
    raw_place = response.json()
    place, created = Place.objects.get_or_create(
        title=raw_place['title'],
        lat=raw_place['coordinates']['lat'],
        lng=raw_place['coordinates']['lng'],
        defaults={
            'short_description': raw_place['description_short'],
            'long_description': raw_place['description_long'],
        },
    )
    return place, raw_place['imgs'], created


def fetch_img(place, img_url, img_num, img_name):
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
