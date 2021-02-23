from django.contrib import admin
from appblog.models import Story, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'pubdate', 'author')
