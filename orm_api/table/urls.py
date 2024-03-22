from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.food, name='food'),
    path('vegetables_fruits/', views.vegetables_fruits, name='vegetables_fruits'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
