from django.shortcuts import render
from django.apps.registry import apps
from Core.plugin_ucitavanje.models import Sampionat, Tim
from UcitavanjeKod.ucitavanje.kod.ucitavanje_kod import UcitatiCSVKod
import copy

def tree_layout(request):
    term = request.GET.get('search')
    filter = request.GET.get('filter')
    plugini = apps.get_app_config('plugin_ucitavanje').plugini_ucitavanje


    sampionati = copy.deepcopy(apps.get_app_config('plugin_ucitavanje').sampionati)
    sampionat = sampionati["2002"]

    if term is not None:

        for faza in sampionat.faze:
            utakmice = []
            for utakmica in faza.utakmice:
                if term.capitalize() in utakmica.gost.naziv or term.capitalize() in utakmica.domacin.naziv:
                    utakmice.append(utakmica)
            faza.utakmice = utakmice

    if filter is not None:
        for faza in sampionat.faze:
            utakmice = []
            for utakmica in faza.utakmice:
                rezultat1, rezultat2 = utakmica.rezultat.split(":")
                if int(rezultat1) >= int(filter) or int(rezultat2) >= int(filter):
                    utakmice.append(utakmica)
            faza.utakmice = utakmice

    return render(request, "tree.html", {"sampionati": [sampionat], "title": "Tree layout",
                                         "plugin_ucitavanje": sampionati})


def force_layout(request):
    term = request.GET.get('search')
    filter = request.GET.get('filter')
    sampionati = copy.deepcopy(apps.get_app_config('plugin_ucitavanje').sampionati)
    sampionat = sampionati["2002"]

    if term is not None:

        for faza in sampionat.faze:
            utakmice = []
            for utakmica in faza.utakmice:
                if term.capitalize() in utakmica.gost.naziv or term.capitalize() in utakmica.domacin.naziv:
                    utakmice.append(utakmica)
            faza.utakmice = utakmice


    if filter is not None:
        for faza in sampionat.faze:
            utakmice = []
            for utakmica in faza.utakmice:
                rezultat1, rezultat2 = utakmica.rezultat.split(":")
                if int(rezultat1) >= int(filter) or int(rezultat2) >= int(filter):
                    utakmice.append(utakmica)
            faza.utakmice = utakmice

    return render(request, "force.html", {"sampionati": [sampionat], "title": "Force layout",
                                          "plugin_ucitavanje": sampionati})


def zoom_pan():
    return ".call(d3.behavior.zoom().on(\"zoom\", function () { svg.attr(\"transform\", " \
           "\"translate(\" + d3.event.translate + \")\" + \"scale(\" + d3.event.scale + \")\")}))"
