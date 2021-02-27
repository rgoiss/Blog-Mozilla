from django.shortcuts import render
from appblog.models import Author, Story


def index(request):
    """View for the home page."""

    num_stories = Story.objects.all().count()
    num_authors = Author.objects.all().count()

    context = {
        'num_stories': num_stories,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)
