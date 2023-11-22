from django.db import models

from recipes.models import Image, IngredientCategory
# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=255)