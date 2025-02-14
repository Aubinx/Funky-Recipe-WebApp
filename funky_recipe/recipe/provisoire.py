def recetteroulette(request):
    global message
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
        m3 = '<a href="http://127.0.0.1:8000/recetteroulette/"><input type="button" value="Faire une autre recherche"></a>'
        for i in range(ln):
            names[i] = '<a href='+links[i]+'><strong>'+names[i]+'</strong></a>'
            names[i] += '<br>'+ingredients[i].capitalize()+'<br>'+'<br>'
        if len(id_i) == 0:
            m1 = "Malheureusement, aucun de vos ingrédients n'est valide :( <br>Essayez avec d'autres ingrédients !"
            m2 = ''
        else:
            m1 = '<strong>Vous avez entré les ingrédients :</strong>' + \
                '<ul><li>'+'<li>'.join(l)+'</ul>'
            if ln == 0:
                m2 = "Malheureusement, aucune de nos recettes ne contient tous vos ingrédients :( <br>Essayez avec d'autres ingrédients !"
            elif ln == 1:
                m2 = '<strong>Nous vous proposons la recette suivantes :</strong>' + \
                    '<ul><li>'+'<li>'.join(names)+'</ul>'
            else:
                m2 = f'<strong>Nous vous proposons les {ln} recettes suivantes :</strong>' + \
                    '<ul><li>'+'<li>'.join(names)+'</ul>'
        message = '<div style="font-family: system-ui">'+m1+m2+m3+'</div>'
        template = loader.get_template("./recipe/resultats.html")
        return HttpResponse(template.render(request=request))