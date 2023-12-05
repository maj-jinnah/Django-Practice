from django.shortcuts import render
import datetime

# Create your views here.


def app(request):
    return render(request, 'template_filtering/app.html')


def about(request):
    return render(request, 'template_filtering/about.html')


def contract(request):
    return render(request, 'template_filtering/contract.html')


def filtering(request):
    data = {'fname': 'Mohammad Ali', 'lname': 'jinnah', 'age': 25, 'list': ['A', 'B', 'C', 'D', 'E'], 'date': datetime.datetime.now(), 'nothing': '',
            'title': "This is an example with <b>HTML</b> tags",
            'linenumbers': 'one\ntwo\nthree',
            'courses': [
        {
            'id': 1,
            'name': 'C/C++',
            'fee': 2500
        },
        {
            'id': 2,
            'name': 'Data Structure',
            'fee': 4500
        },
        {
            'id': 3,
            'name': 'Algorithms',
            'fee': 5000
        },
        {
            'id': 4,
            'name': 'Python',
            'fee': 3500
        },
        {
            'id': 5,
            'name': 'OOP',
            'fee': 3000
        },
    ]}
    return render(request, 'template_filtering/filtering.html', data)
