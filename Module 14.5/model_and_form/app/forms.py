from django import forms
from django.forms.widgets import NumberInput
import datetime
from .models import MyModel, My_Model

# Create your forms here.
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]


class ExampleForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    email_addrss = forms.EmailField(required=True)
    message = forms.CharField(max_length=10, min_length=3)
    email_address = forms.CharField(
        label='Please enter your email address')
    first_name = forms.CharField(initial='Your name: ')
    agree = forms.BooleanField(initial=True)
    day = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color1 = forms.ChoiceField(
        widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors2 = forms.MultipleChoiceField(
        choices=FAVORITE_COLORS_CHOICES)
    favorite_colors3 = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES,)
    model_choice = forms.ModelChoiceField(
        queryset=My_Model.objects.all(),
        initial=0,
        empty_label="Select a model"
    )
    model_choices = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=My_Model.objects.all(),
        initial=0
    )

class MyModelForm(forms.ModelForm):
    
    class Meta:
        model = MyModel
        fields = '__all__'
