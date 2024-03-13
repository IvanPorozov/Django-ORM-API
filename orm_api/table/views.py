from django.shortcuts import render

from .models import Food


def index(request):
    if request.method == 'POST':
        form = Food(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Food()
    return render(request, 'table.html', {'a': 1})
