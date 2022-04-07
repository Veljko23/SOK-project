from setuptools import setup, find_packages

setup(
    name="ucitavanje-kod",
    version="0.1",
    packages=find_packages(),
    install_requires=['plugin_ucitavanje>=0.1'],
    entry_points = {
        'parser.ucitati':
            ['ucitavanje_kod=ucitavanje.kod.ucitavanje_kod:UcitatiCSVKod'],
    },
    data_files=[('fajl', ['fajl/WorldCupMatches.csv'])],
    zip_safe=False
)