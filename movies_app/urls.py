from django.contrib import admin
from django.urls import path
from .views import MovieView, CollectionListView, CollectionDetailsView, RequestCountView

urlpatterns = [
    path('get_movie/', MovieView.as_view()),
    path('collection/', CollectionListView.as_view()),
    path('collection/<uuid:collection_uuid>/', CollectionDetailsView.as_view()),
    path('request/', RequestCountView.as_view()),
    path('request/reset/', RequestCountView.as_view())
]