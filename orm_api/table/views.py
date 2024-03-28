from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from .forms import AddNewElementForm
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
    vegetables_type = FoodType.objects.get(name='Овощ')
    vegetables = Food.objects.filter(type=vegetables_type)
    fruits_type = FoodType.objects.get(name='Фрукт')
    fruits = Food.objects.filter(type=fruits_type)
    return render(request, 'main.html', {'vegetables': vegetables, 'fruits': fruits})


def vegetables_fruits(request):
    sort_by = request.GET.get('sort_by', 'name')
    vegetables_type = FoodType.objects.get(name='Овощ')
    fruits_type = FoodType.objects.get(name='Фрукт')
    foods = Food.objects.all()

    if sort_by is None:
        return
    elif sort_by == 'vegetables':
        foods = foods.filter(type=vegetables_type)
    elif sort_by == 'fruits':
        foods = foods.filter(type=fruits_type)
    elif sort_by == 'alpha':
        foods = foods.order_by('name')

    context = {
        'foods': foods,
    }
    return render(request, 'vegetables_fruits.html', context)


def add_new_element(request):
    if request.method == 'POST':
        form = AddNewElementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = AddNewElementForm()
    return render(request, 'add_new_element.html', {'form': form})


def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    return render(request, 'food_detail.html', {'food': food})
