from django.shortcuts import render
from .models import Food, FoodType


def food(request):
    vegetables_type = FoodType.objects.get(name='Vegetables')
    vegetables = Food.objects.filter(type=vegetables_type)
    fruits_type = FoodType.objects.get(name='Fruits')
    fruits = Food.objects.filter(type=fruits_type)
    return render(request, 'main.html', {'vegetables': vegetables, 'fruits': fruits})


def vegetables_fruits(request):
    foods = Food.objects.all()
    return render(request, 'vegetables_fruits.html', {'foods': foods})

