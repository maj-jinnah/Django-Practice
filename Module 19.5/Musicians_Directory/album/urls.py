from django.urls import path
from .views import AlbumView, EditAlbumView, DeleteAlbumView
from .import views

urlpatterns = [
    path('', AlbumView.as_view(), name='album'),
    path('edit/<int:id>/', EditAlbumView.as_view(), name='edit_album'),
    path('delete/<int:id>/', DeleteAlbumView.as_view(), name='delete_album'),
]