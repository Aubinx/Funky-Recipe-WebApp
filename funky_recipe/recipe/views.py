from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from recipe.models import Ingredient, Recette
from urllib.parse import unquote
from html.parser import HTMLParser


def index(request):
    template = loader.get_template("./recipe/index.html")
    return HttpResponse(template.render(request=request))


def ordre(x): return x[1]

messageroulette:str = ''
messageaddrecipe:str = ''

def recetteroulette(request):
    global messageroulette
    if request.GET == {} or (request.GET['i1'] == '' and request.GET['i2'] == '' and request.GET['i3'] == '' and request.GET['i4'] == '' and request.GET['i5'] == ''):
        template = loader.get_template("./recipe/recetteroulette.html")
        return HttpResponse(template.render(request=request))
    else:
        d = request.GET
        l = []
        for i in (d['i1'].capitalize(), d['i2'].capitalize(), d['i3'].capitalize(), d['i4'].capitalize(), d['i5'].capitalize()):
            if i not in l and i in [ingredient.name for ingredient in Ingredient.objects.all()]:
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
                id_r.append((str(i.id), len(i.id_ing.all())))
        id_r.sort(key=ordre)
        id_r = [i[0] for i in id_r]
        results = [Recette.objects.get(id=i) for i in id_r]
        names = [i.name for i in results]
        links = [i.link for i in results]
        ingredients_id = [i.id_ing.all() for i in results]
        ingredients1 = []
        for i in ingredients_id:
            k = [j.name for j in i]
            ingredients1.append(k)
        ingredients = [', '.join(i) for i in ingredients1]
        ln = len(names)
        m3 = '<a class="btn btn-primary" href="http://127.0.0.1:8000/recetteroulette/">Faire une autre recherche</a>'
        for i in range(ln):
            names[i] = '<a href='+links[i]+'><strong>'+names[i]+'</strong></a>'
            names[i] += '<br>'+ingredients[i].capitalize()+'<br>'+'<br>'
        if len(id_i) == 0:
            m1 = "Malheureusement, aucun de vos ingrédients n'est valide :( <br>Essayez avec d'autres ingrédients !"
            m2 = '<br><br>'
        else:
            m1 = '<strong>Vous avez entré les ingrédients :</strong>' + '<br><br>' + '<ul><li>'+'<li>'.join(l)+'</ul>'
            if ln == 0:
                m2 = "Malheureusement, aucune de nos recettes ne contient tous vos ingrédients :( <br>Essayez avec d'autres ingrédients !<br><br>"
            elif ln == 1:
                m2 = '<strong>Nous vous proposons la recette suivante :</strong>' + '<br><br>' + '<ul><li>'+'<li>'.join(names)+'</ul>'
            else:
                m2 = f'<strong>Nous vous proposons les {ln} recettes suivantes :</strong>' + '<br><br>' + '<ul><li>'+'<li>'.join(names)+'</ul>'
        messageroulette = '<div style="font-family: system-ui">'+m1+m2+m3+'</div>'
        template = loader.get_template("./recipe/resultats.html")
        return HttpResponse(template.render(request=request))

def globalmessage():
    global messageroulette
    return messageroulette

def about(request):
    template = loader.get_template("./recipe/about.html")
    return HttpResponse(template.render(request=request))


def contact(request):
    template = loader.get_template("./recipe/contact.html")
    return HttpResponse(template.render(request=request))


def gastronotrip(request):
    if request.GET == {}:
        template = loader.get_template("./recipe/gastronotrip.html")
        return HttpResponse(template.render(request=request))
    else:
        pays = request.GET['my_html_select_box']
        if pays == 'Italie':
            template = loader.get_template("./recipe/italie.html")
            return HttpResponse(template.render(request=request))
        if pays == 'Maroc':
            template = loader.get_template("./recipe/maroc.html")
            return HttpResponse(template.render(request=request))
        if pays == 'Mexique':
            template = loader.get_template("./recipe/mexique.html")
            return HttpResponse(template.render(request=request))


def addrecipe(request):
    global messageaddrecipe
    if request.GET == {} or (request.GET['nom'] == '' and request.GET['lien'] == '' and request.GET['ing'] == ''):
        template = loader.get_template("./recipe/addrecipe.html")
        return HttpResponse(template.render(request=request))
    else:
        d = request.GET
        (a, b, c) = (d['nom'], d['ing'], d['lien'])
        l = b.split(', ')
        m1 = "<strong style='font-size: 2em'>Titre : "+a+"</strong><br><br>"
        m2 = '<strong>Vous avez entré les ingrédients :</strong>' + \
            '<ul><li>'+'<li>'.join(l)+'</ul>'
        m3 = "<br><strong>Description de la recette :</strong><br>"+'<br>'+c + '<br><br><br>'
        m4 = '<a class="btn btn-primary" href="http://127.0.0.1:8000/addrecipe/"> Annuler </a> '
        m5 = '<a href="javascript:history.go(-1)" class="btn btn-primary">Revenir en arrière</a> '
        m6 = '<a class="btn btn-primary" href="#!"> Confirmer </a>'
        m = '<div style="font-family: system-ui">'+m1+m2+m3+m4+m5+m6+'</div>'
        messageaddrecipe = m
        template = loader.get_template("./recipe/resultsaddrecipe.html")
        return HttpResponse(template.render(request=request))

def globalmessageaddrecipe():
    global messageaddrecipe
    return messageaddrecipe
