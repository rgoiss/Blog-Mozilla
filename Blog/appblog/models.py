from django.db import models
from django.urls import reverse
from django.conf import settings


class Author(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    bio = models.TextField()

    def get_absolute_url(self):
        return reverse('sigle-author', args=[str(self.id)])

    def __str__(self):
        return str(self.user.username)


class Story(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    report = models.TextField()
    pubdate = models.DateTimeField(auto_now=True, editable=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:

        ordering = ['-pubdate']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('story-detail', kwargs={'slug': self.slug})


class Comments(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    story = models.ForeignKey(
        Story, on_delete=models.CASCADE, blank=True, null=True
    )
    comment = models.TextField()
    published_in = models.DateTimeField(auto_now=True, editable=False)

    class Meta:

        ordering = ['-published_in']

    def __str__(self):
        return self.comment
