from django.db import models

# Create your models here.

class Recette(models.Model):
    id_rec = models.IntegerField(unique=True)
    name_rec = models.CharField()
    link = models.CharField()

class Ingredient(models.Model):
    id_ing = models.IntegerField(unique=True)
    name_ing = models.CharField()
    id_rec = models.ManyToManyField(Recette)