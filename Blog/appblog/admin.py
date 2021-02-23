from django.contrib import admin
from appblog.models import Author, Comments, Story


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('comment', 'published_in', 'story')


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'pubdate', 'author')
