from django.shortcuts import render
from rest_framework import viewsets

from .models import Food
from .models import FoodType
from .serializers import FoodSerializer, FoodTypeSerializer


class FoodTypeViewSet(viewsets.ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


def food(request):
    vegetables_type = FoodType.objects.get(name='Vegetables')
    vegetables = Food.objects.filter(type=vegetables_type)
    fruits_type = FoodType.objects.get(name='Fruits')
    fruits = Food.objects.filter(type=fruits_type)
    return render(request, 'main.html', {'vegetables': vegetables, 'fruits': fruits})


def vegetables_fruits(request):
    sort_by = request.GET.get('sort_by', 'name')
    fruit_checked = request.GET.get('fruit') == 'on'
    vegetable_checked = request.GET.get('vegetable') == 'on'

    foods = Food.objects.all()
    if fruit_checked and vegetable_checked:
        foods = foods.filter(type__name__in=['Фрукты', 'Овощи'])
    elif fruit_checked:
        foods = foods.filter(type__name='Фрукты')
    elif vegetable_checked:
        foods = foods.filter(type__name='Овощи')

    if sort_by == 'useful_elements_asc':
        foods = foods.order_by('useful_elements')
    elif sort_by == 'useful_elements_desc':
        foods = foods.order_by('-useful_elements')
    else:
        foods = foods.order_by('name')

    context = {
        'foods': foods,
        'fruit_checked': fruit_checked,
        'vegetable_checked': vegetable_checked,
    }
    return render(request, 'vegetables_fruits.html', context)
