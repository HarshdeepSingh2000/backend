# urls.py

from django.urls import path
from .views import register_user, MovieListView, CollectionListView, CollectionCreateView, CollectionDetailView, request_count, reset_request_count

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('movies/', MovieListView.as_view(), name='movie_list'),
    path('collection/', CollectionListView.as_view(), name='collection_list'),
    path('collection/create/', CollectionCreateView.as_view(), name='collection_create'),
    path('collection/<uuid:collection_uuid>/', CollectionDetailView.as_view(), name='collection_detail'),
    path('request-count/', request_count, name='request_count'),
    path('request-count/reset/', reset_request_count, name='reset_request_count'),
]

