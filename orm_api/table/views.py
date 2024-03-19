from django.shortcuts import render

from .models import Food


def food(request):
    food = Food.objects.filter()
    return render(request, 'table.html', {'food': food})
