from django.db import models
from django.shortcuts import reverse
from django.utils import timezone

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name
    
# Model for recipe.

class Recipe(models.Model):
    # class attributes
    description = models.TextField(max_length=400)
    cooking_time = models.FloatField(
        help_text="in minutes"
    )  # Using FloatField for precision
    ingredients = models.ManyToManyField(Ingredient)
    image = models.ImageField(upload_to="recipes/", blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def calculate_difficulty(self):
        ingredient_count = self.ingredients.count()
        if self.cooking_time < 10 and ingredient_count < 5:
            return "Easy"
        elif self.cooking_time < 10 and ingredient_count >= 5:
            return "Basic"
        elif self.cooking_time >= 10 and ingredient_count < 5:
            return "Medium"
        else:
            return "Hard"

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"pk": self.pk})
     # string representation
    def __str__(self):
        return str(self.name)

