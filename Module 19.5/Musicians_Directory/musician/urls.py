from django.urls import path
from .views import MusicianView, EditMusicianView

urlpatterns = [
    path('', MusicianView.as_view(), name='musician'),
    path('edit_musician/<int:id>/', EditMusicianView.as_view(), name='edit_musician'),
]