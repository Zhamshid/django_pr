from django.shortcuts import render


def index(request):
    data = {
        'title': 'Басты бет',
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about_us.html')

def contacts(request):
    data = {
        'title':'Байланыстар'
    }
    return render(request, 'main/contacts.html', data)
