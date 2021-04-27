from django.shortcuts import render
from appblog.models import Story, Author
from django.views.generic import ListView, DetailView

from django.shortcuts import get_object_or_404


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


class ListByAuthor(ListView):
    model = Story
    template_name = 'list_by_author.html'

    def get_queryset(self):
        id = self.kwargs['pk']
        sigle_author = get_object_or_404(Author, pk=id)
        return Author.objects.filter(user=sigle_author)

    def get_context_data(self, **kwargs):
        context = super(ListByAuthor, self).get_context_data(**kwargs)
        context['author'] = get_object_or_404(Author, pk=self.kwargs['pk'])
        return context


class StoriesDetail(DetailView):
    models = Story
    template_name = 'story_detail.html'
    queryset = Story.objects.all()
    context_object_name = 'detail'


class AuthorsList(ListView):
    models = Author
    template_name = 'author_list.html'
    queryset = Author.objects.all()
    context_object_name = 'authors'
