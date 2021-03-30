from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('allauthors/', views.AuthorsList.as_view(), name='all-authors'),
    path('allstories/', views.StoriesList.as_view(), name='all-stories'),
    path(
        'allstories/<slug:slug>/',
        views.StoriesDetail.as_view(),
        name='story-detail',
    ),
]
