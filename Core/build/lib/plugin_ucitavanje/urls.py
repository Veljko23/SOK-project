from django.urls import path

from Core.plugin_ucitavanje import sampionat_view
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ucitavanje/plugin/<str:id>', views.ucitavanje_plugin, name="ucitavanje_plugin"),


    path('force/', sampionat_view.force_layout, name="force_layout"),
    path('tree/', sampionat_view.tree_layout, name="tree_layout"),

]