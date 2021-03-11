from django.shortcuts import render
from appblog.models import Story, Author
from django.views.generic import ListView, DetailView


def index(request):
    """View for the home page."""

    num_stories = Story.objects.all().count()
    num_authors = Author.objects.all().count()

    context = {
        'num_stories': num_stories,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)


class StoriesList(ListView):
    models = Story
    template_name = 'story_list.html'
    queryset = Story.objects.all()
    context_object_name = 'stories'


class AuthorsList(ListView):
    models = Author
    template_name = 'author_list.html'
    queryset = Author.objects.all().order_by('-user')[:10]
    context_object_name = 'authors'
