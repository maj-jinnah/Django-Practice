from django.shortcuts import render

# Create your views here.


def app(request):
    return render(request, 'first_app/app.html')

def about(request):
    return render(request, 'first_app/about.html')
def contract(request):
    return render(request, 'first_app/contract.html')
