from django.core.management.base import BaseCommand
from reviews.models import Category, Title, Genre, GenreTitle, Comment, Review
from users.models import User
import csv
from api_yamdb.settings import BASE_DIR

csv_to_models = (
    ('category.csv', Category),
    ('comments.csv', Comment),
    ('genre_title.csv', GenreTitle),
    ('genre.csv', Genre),
    ('review.csv', Review),
    ('titles.csv', Title),
    ('users.csv', User),
)


class Command(BaseCommand):
    help = 'Импорт данных из csv файлов в базу данных'

    def handle(self, *args, **options):
        csv_path = BASE_DIR / 'static/data/'

        for csv_file, _model in csv_to_models:
            file = csv_path / csv_file
            with open(file, encoding='utf-8'):
                rows = csv.DictReader(file, delimiter=';', quotechar='"')
                for row in rows:
                    _model.objects.create(**row)
