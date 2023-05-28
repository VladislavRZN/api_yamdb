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
        return self.name


class Genre(models.Model):
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
       title_category_genres
        return self.title[:STR_LENGTH]
        return self.slug


class Title(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name='Slug категории',
        title_category_genres
    )
    genre = models.ForeignKey(
        Genres,
        verbose_name='Slug жанра',
        on_delete=models.SET_NULL
    )
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle'
    )
    name = models.CharField(
        'Название',
        max_length=256,
    )
    title_category_genres
    year = models.DateTimeField('Год выпуска')
    year = models.IntegerField('Год выпуска')
    description = models.TextField(
        'Описание',
        blank=True,
        null=True
    )

    title_category_genres
    rating = models.FloatField(
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('year', 'name')
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        default_related_name = 'titles'

    def __str__(self):
        return self.text[:STR_LENGTH]



class GenreTitle(models.Model):
    genre_id = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    title_id = models.ForeignKey(
        Title,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.genre} {self.title}'
