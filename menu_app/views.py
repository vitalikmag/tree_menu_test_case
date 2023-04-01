from django.shortcuts import render


def index(request, name):
    return render(request, 'menu_app/index.html', {'name': name})
