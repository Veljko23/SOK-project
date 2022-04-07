from django.apps.registry import apps
from django.shortcuts import render
from projekat.ucitavanje import ucitavanje



def tree_layout(request):
    term = request.GET.get('search')
    filter = request.GET.get('filter')

    if term is None:
        term = ''

    if filter is None:
        filter = '0'

    sampionati = ucitavanje(term, filter)
    timovi = ucitavanje(term, filter)

    return render(request, "tree.html", {"sampionati":[sampionati["2002"]], "timovi":timovi, "title":"Tree layout"})

def index(request):

    return render(request, "index.html", {"title": "Index"})

def force_layout(request):
    term = request.GET.get('search')
    filter = request.GET.get('filter')
    if term is None:
        term = ''

    if filter is None:
        filter = '0'

    sampionati = ucitavanje(term, filter)
    return render(request, "force.html", {"sampionati":[sampionati["2002"]], "title":"Force layout"})

def collapse_layout(request):

    term = request.GET.get('search')
    filter = request.GET.get('filter')
    if term is None:
        term = ''

    if filter is None:
        filter = '0'

    sampionati = ucitavanje(term, filter)
    return render(request, "collapse.html", {"sampionati":[sampionati["2002"]], "title":"Collapse layout"})

def zoom_pan():
    return ".call(d3.behavior.zoom().on(\"zoom\", function () { svg.attr(\"transform\", " \
           "\"translate(\" + d3.event.translate + \")\" + \"scale(\" + d3.event.scale + \")\")}))"
