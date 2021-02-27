from django.contrib import admin
from appblog.models import User, Author, Story, Comments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'pubdate', 'author')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('comment', 'published_in', 'story')
