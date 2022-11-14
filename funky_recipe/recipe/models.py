from django.db import models

# Create your models here.

class Recette(models.Model):
    id_rec = models.IntegerField(unique=True)
    name_rec = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

class Ingredient(models.Model):
    id_ing = models.IntegerField(unique=True)
    name_ing = models.CharField(max_length=200)
    id_rec = models.ManyToManyField(Recette)
