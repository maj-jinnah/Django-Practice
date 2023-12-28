from django.shortcuts import render, redirect
from .import forms, models
from django.views import View

# Create your views here.
class MusicianView(View):
    template_name = 'musician.html'

    def get(self, request):
        musician_form = forms.MusicianForm()
        return render(request, self.template_name, {'form': musician_form})

    def post(self, request):
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')
        return render(request, self.template_name, {'form': musician_form})

class EditMusicianView(View):
    template_name = 'musician.html'

    def get(self, request, id):
        musician = models.Musician.objects.get(pk=id)
        musician_form = forms.MusicianForm(instance=musician)
        return render(request, self.template_name, {'form': musician_form})

    def post(self, request, id):
        musician = models.Musician.objects.get(pk=id)
        musician_form = forms.MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')
        return render(request, self.template_name, {'form': musician_form})