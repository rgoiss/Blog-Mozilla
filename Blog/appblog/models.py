import uuid
from django.db import models


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, help_text='Author name')
    description = models.CharField(
        max_length=200, help_text='Say something about you'
    )

    def __str__(self):
        return self.name


class Story(models.Model):
    title = models.CharField(max_length=30)
    report = models.TextField()
    pubdate = models.DateTimeField(auto_now=True, editable=False)
    author = models.ForeignKey(
        'Author', on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.title
