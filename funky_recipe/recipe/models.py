from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=200)

class Recette(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    cat = models.CharField(max_length=200)
    id_ing = models.ManyToManyField(Ingredient)
