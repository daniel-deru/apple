from django.db import models

class Image(models.Model):
    image_url = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.image_url
    
class DietLabel(models.Model):
    label = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.label
    
class HealthLabel(models.Model):
    label = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.label
    
class Caution(models.Model):
    caution = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.caution
    
class IngredientCategory(models.Model):
    category = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.category
    
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    quantity = models.FloatField()
    measure = models.CharField()
    weight = models.FloatField()
    category = models.CharField()
    image = models.OneToOneField(Image)

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    recipe_yield = models.FloatField()
    calories = models.FloatField()
    total_weight = models.FloatField()
    total_time = models.FloatField()
    images = models.ManyToManyField(Image)
    diet_labels = models.ManyToManyField(DietLabel)
    health_labels = models.ManyToManyField(HealthLabel)
    cautions = models.ManyToManyField(Caution)
    
    def __str__(self) -> str:
        return self.name
    
    