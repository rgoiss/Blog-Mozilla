from django.contrib import admin
from appblog.models import Author, Story, Comments


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'pubdate', 'author')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('comment', 'published_in', 'story')
