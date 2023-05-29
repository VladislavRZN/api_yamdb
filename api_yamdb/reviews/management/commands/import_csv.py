import csv
from collections import namedtuple

from django.conf import settings
from django.core.management import BaseCommand
from django.db.utils import IntegrityError
from reviews.models import (Category, Comment, Genre, GenreTitle, Review,
                            Title)
from users.models import User

model_tuple = namedtuple('Model', ['csv_file', 'model', 'fields'])

user = model_tuple(
    'users.csv',
    User,
    ['id', 'username', 'email', 'role', 'bio', 'first_name', 'last_name'])
category = model_tuple(
    'category.csv',
    Category,
    ['id', 'name', 'slug'])
genre = model_tuple(
    'genre.csv',
    Genre,
    ['id', 'name', 'slug'])
title = model_tuple(
    'titles.csv',
    Title,
    ['id', 'name', 'year', 'category_id'])
review = model_tuple(
    'review.csv',
    Review,
    ['id', 'title_id', 'text', 'author_id', 'score', 'pub_date'])
comment = model_tuple(
    'comments.csv',
    Comment,
    ['id', 'review_id', 'text', 'author_id', 'pub_date'])
genre_title = model_tuple(
    'genre_title.csv',
    GenreTitle,
    ['id', 'title_id', 'genre_id'])

models = (user, category, genre, title, genre_title, review, comment, )


class Command(BaseCommand):
    help = 'Импорт данных из csv файлов в базу данных'

    def handle(self, *args, **kwargs):
        for model in models:
            try:
                with open(f'{settings.BASE_DIR}/static/data/{model.csv_file}',
                          'r', encoding='utf-8') as csv_file:
                    rows = csv.DictReader(csv_file)
                    if rows.fieldnames != model.fields:
                        raise BaseException(
                            f'Поля в файле {model.base}'
                            f'должны соответствовать: {model.fields}')
                    model.model.objects.bulk_create(
                        model.model(**row) for row in rows)
            except IntegrityError:
                pass
            except FileNotFoundError:
                raise BaseException(
                    f'В директории {settings.BASE_DIR}/static/data/'
                    f'Не обнаружен файл {model.csv_file}')
        self.stdout.write(self.style.SUCCESS('Данные импортированы'))
