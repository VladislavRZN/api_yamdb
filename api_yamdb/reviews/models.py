from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import User


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
        return self.slug


class Title(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name='Slug категории',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle'
    )
    name = models.CharField(
        'Название',
        max_length=256,
    )
    year = models.IntegerField('Год выпуска')

    description = models.TextField(
        'Описание',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('year', 'name')
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        default_related_name = 'titles'

    def __str__(self):
        return self.name


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


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    pub_date = models.DateTimeField(
        'Дата отзыва',
        auto_now_add=True,
        db_index=True
    )
    text = models.TextField()
    score = models.IntegerField(
        'Оценить',
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ],
    )

    class Meta:
        ordering = ['-pub_date']
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'], name="unique_review")
        ]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления",
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ('created',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        default_related_name = 'comments'

    def __str__(self):
        return self.author
