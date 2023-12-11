from django.shortcuts import render
# from . forms import ExampleForm
from . forms import MyModelForm

# Create your views here.


def home(request):
    # form = ExampleForm()
    form = MyModelForm()
    return render(request, 'home.html', {'form': form})
