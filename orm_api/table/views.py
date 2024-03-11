from django.shortcuts import render


def index(request):
    return render(request, 'table.html', {'a': 'gg'})
