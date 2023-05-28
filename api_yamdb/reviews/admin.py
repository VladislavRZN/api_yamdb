from django.contrib import admin

from .models import Comment, Review, Title, Category, Genre


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'description')
    search_fields = ('description', 'name')
    list_filter = ('category', 'year')
    list_editable = ('description',)
    empty_value_display = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name',)
    list_editable = ('slug',)
    empty_value_display = '-пусто-'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name',)
    list_editable = ('slug',)
    empty_value_display = '-пусто-'


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'score', 'author', 'title')
    search_fields = ('title', 'author')
    list_filter = ('score', 'text',)
    empty_value_display = '-пусто-'


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment)
admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)
