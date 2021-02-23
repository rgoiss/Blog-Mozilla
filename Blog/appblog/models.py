import uuid
from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=20, help_text='Author name')
    bio = models.TextField()

    def __str__(self):
        return self.name


class Story(models.Model):
    title = models.CharField(max_length=30)
    report = models.TextField()
    pubdate = models.DateTimeField(auto_now=True, editable=False)
    author = models.ForeignKey(
        'Author', on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:

        ordering = ['-pubdate']

    def __str__(self):
        return self.title


class Comments(models.Model):
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, blank=True, null=True
    )
    story = models.ForeignKey(
        'Story', on_delete=models.CASCADE, blank=True, null=True
    )
    comment = models.TextField()
    published_in = models.DateTimeField(auto_now=True, editable=False)

    class Meta:

        ordering = ['-published_in']

    def __str__(self):
        return self.comment
