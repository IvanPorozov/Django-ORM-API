from django.db import models


class FoodType(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    img = models.ImageField(blank=True)
    type = models.ForeignKey(FoodType, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name
