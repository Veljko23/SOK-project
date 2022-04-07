from django.apps.registry import apps
from django.shortcuts import render, redirect


def index(request):
    plugini = apps.get_app_config('plugin_ucitavanje').plugini_ucitavanje
    return render(request,"index.html",{"title":"Index","plugini_ucitavanje":plugini})

def ucitavanje_plugin(request,id):

    plugini=apps.get_app_config('plugin_ucitavanje').plugini_ucitavanje
    for i in plugini:
        if i.identifier() == id:
            apps.get_app_config('plugin_ucitavanje').sampionati=i.ucitati()
    return redirect('index')