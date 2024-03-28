from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FoodViewSet, FoodTypeViewSet
from . import views

router = DefaultRouter()
router.register(r'foodtypes', FoodTypeViewSet)
router.register(r'foods', FoodViewSet)

urlpatterns = [
    path('', views.food, name='food'),
    path('vegetables_fruits/', views.vegetables_fruits, name='vegetables_fruits'),
    path('api/food_list/', include(router.urls)),
    path('add_new_element/', views.add_new_element, name='add_new_element'),
    path('food/<int:pk>/', views.food_detail, name='food_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
