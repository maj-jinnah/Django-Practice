from django.shortcuts import render, redirect
from django.views import View
from . import forms, models

# Create your views here.
class AlbumView(View):
    template_name = 'album.html'

    def get(self, request):
        album_form = forms.AlbumForm()
        return render(request, self.template_name, {'form': album_form})

    def post(self, request):
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
        return render(request, self.template_name, {'form': album_form})

class EditAlbumView(View):
    template_name = 'album.html'

    def get(self, request, id):
        album = models.Album.objects.get(pk=id)
        album_form = forms.AlbumForm(instance=album)
        return render(request, self.template_name, {'form': album_form})

    def post(self, request, id):
        album = models.Album.objects.get(pk=id)
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
        return render(request, self.template_name, {'form': album_form})

class DeleteAlbumView(View):
    def get(self, request, id):
        album = models.Album.objects.get(pk=id)
        album.delete()
        return redirect('home')