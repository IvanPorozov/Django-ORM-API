from django.db import models


class FoodType(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(max_length=500, verbose_name="Текст статьи")
    img = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    type = models.ForeignKey(FoodType, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name
