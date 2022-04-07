from setuptools import setup, find_packages

setup(
    name="plugin_ucitavanje",
    version="0.1",
    packages=find_packages(),
    install_requires=['Django>=2.1'],

    package_data={'plugin_ucitavanje': ['templates/*.html']},
    zip_safe=False
)