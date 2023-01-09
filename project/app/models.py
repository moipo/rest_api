from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length = 200, blank = True, default = "")
    price = models.FloatField(blank = True, null = True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length = 200, blank = True, default = "")
    callories = models.IntegerField(blank = True, null = True)
    weight = models.IntegerField(blank = True, null = True)

    def __str__(self):
        return self.name


class IngredientItem(models.Model):
    recipe = models.ForeignKey("Recipe", blank = True, null = True, on_delete = models.CASCADE)
    ingredient = models.ForeignKey("Ingredient", blank = True, null = True, on_delete = models.CASCADE)
    amount = models.IntegerField(blank = True, null = True)

    def __str__(self):
        return str(self.amount) + " " + str(self.ingredient.name)
