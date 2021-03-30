import uuid
from django.db import models
from django.urls import reverse


class User(models.Model):
    name = models.CharField(max_length=20)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, blank=True, null=True
    )
    bio = models.TextField()

    def __str__(self):
        return str(self.user)


class Story(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    report = models.TextField()
    pubdate = models.DateTimeField(auto_now=True, editable=False)
    author = models.ForeignKey(
        'User', on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:

        ordering = ['-pubdate']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'story-detail', kwargs={'slug': self.slug}
        )


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
