from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from recipe.models import Ingredient, Recette

def index(request):
    template = loader.get_template("./recipe/index.html")
    return HttpResponse(template.render(request=request))


def recetteroulette(request):
    template = loader.get_template("./recipe/recetteroulette.html")
    return HttpResponse(template.render(request=request))

def rrresults(request, s):
    l = [int(i) for i in s.split('-')]
    results = [Recette.objects.get(id=i) for i in l]
    names = [i.name for i in results]
    links = [i.link for i in results]
    ingredients_id = [i.id_ing.all() for i in results]
    ingredients1 = []
    for i in ingredients_id:
        k=[j.name for j in i]
        ingredients1.append(k)
    ingredients = [', '.join(i) for i in ingredients1]
    for i in range(len(names)):
        names[i]='<a href='+links[i]+'><strong>'+names[i]+'</strong></a>'
        names[i]+='<br>'+ingredients[i].capitalize()+'<br>'+'<br>'
    message = '<ul><li>'+'<li>'.join(names)+'</ul>'
    return HttpResponse(message)
