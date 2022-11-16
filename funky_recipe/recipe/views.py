from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from recipe.models import Ingredient, Recette
from urllib.parse import unquote

def index(request):
    template = loader.get_template("./recipe/index.html")
    return HttpResponse(template.render(request=request))


def recetteroulette(request):
    if request.GET=={} or (request.GET['i1']=='' and request.GET['i2']=='' and request.GET['i3']=='' and request.GET['i4']=='' and request.GET['i5']==''):
        template = loader.get_template("./recipe/recetteroulette.html")
        return HttpResponse(template.render(request=request))
    else:
        d = request.GET
        l=[]
        for i in (d['i1'].capitalize(),d['i2'].capitalize(),d['i3'].capitalize(),d['i4'].capitalize(),d['i5'].capitalize()):
            if i not in l and i in [ingredient.name for ingredient in Ingredient.objects.all()] :
                l.append(i)
        id_i = [Ingredient.objects.get(name=i).id for i in l]
        recettes = Recette.objects.all()
        id_r = []
        for i in recettes:
            b = True
            for k in id_i:
                if k not in [j.id for j in i.id_ing.all()]:
                    b = False
            if b:
                id_r.append(str(i.id))    
        results = [Recette.objects.get(id=i) for i in id_r]
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

def results(request, s):
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

def about(request):
    template = loader.get_template("./recipe/about.html")
    return HttpResponse(template.render(request=request))

def contact(request):
    template = loader.get_template("./recipe/contact.html")
    return HttpResponse(template.render(request=request))

