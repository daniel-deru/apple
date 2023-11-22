from django.db import models

# Create your models here.
    
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

class MealType(models.Model):
    type = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.type
    
class CuisineType(models.Model):
    type = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.type
    
class DishType(models.Model):
    type = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.type
    

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    recipe_yield = models.FloatField()
    url = models.CharField(max_length=255)
    calories = models.FloatField()
    total_weight = models.FloatField()
    total_time = models.FloatField()
    
    diet_labels = models.ManyToManyField(DietLabel)
    health_labels = models.ManyToManyField(HealthLabel)
    cautions = models.ManyToManyField(Caution)
    meal_type = models.ManyToManyField(MealType)
    cuisine_type = models.ManyToManyField(CuisineType)
    dish_type = models.ManyToManyField(DishType)
    
    def __str__(self) -> str:
        return self.name
    
class Nutrient(models.Model):
    label = models.CharField(max_length=255)
    total = models.FloatField()
    daily = models.FloatField()
    unit = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    

class SubNutrient(models.Model):
    label = models.CharField(max_length=255)
    total = models.FloatField()
    daily = models.FloatField()
    unit = models.CharField(max_length=255)
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    
class IngredientCategory(models.Model):
    category = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.category
    
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    quantity = models.FloatField()
    measure = models.CharField(max_length=255)
    weight = models.FloatField()
    
    category = models.OneToOneField(IngredientCategory, on_delete=models.CASCADE)
    
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name

class Image(models.Model):
    image_url = models.CharField(max_length=1000)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=True, null=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.image_url
    
    