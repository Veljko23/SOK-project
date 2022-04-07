import pkg_resources
from django.apps import AppConfig


class PluginUcitavanjeConfig(AppConfig):
    name = 'plugin_ucitavanje'
    plugini_ucitavanje=[]

    def ready(self):
        self.plugini_ucitavanje=load_plugins("parser.ucitati")

def load_plugins(oznaka):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=oznaka):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()
        plugins.append(plugin)
    return plugins
