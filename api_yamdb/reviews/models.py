from django.db import models

STR_LENGTH = 15


class Category(models.Model):
    name = models.CharField(
        'Название',
        max_length=256,
    )
    slug = models.SlugField(
        'Слаг',
        max_length=50,
        unique=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title[:STR_LENGTH]


class Genres(models.Model):
    name = models.CharField(
        'Название',
        max_length=256,
    )
    slug = models.SlugField(
        'Слаг',
        max_length=50,
        unique=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.title[:STR_LENGTH]


class Title(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name='Slug категории',
    )
    genre = models.ForeignKey(
        Genres,
        verbose_name='Slug жанра',
    )
    name = models.CharField(
        'Название',
        max_length=256,
    )
    year = models.DateTimeField('Год выпуска')

    description = models.TextField(
        'Описание',
        blank=True,
        null=True
    )

    rating = models.FloatField(
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('year',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        default_related_name = 'titles'

    def __str__(self):
        return self.text[:STR_LENGTH]
