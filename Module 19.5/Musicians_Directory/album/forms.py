from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'date_field': forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker'}),}