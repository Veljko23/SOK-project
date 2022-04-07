import os

from Core.plugin_ucitavanje.models import Sampionat, Tim, Utakmica
from Core.plugin_ucitavanje.services.ucitati import UcitatiService


def apsolutnaPutanja(fajl):
    return os.path.join(os.path.dirname(__file__), "..", "..", "fajl", fajl)

class UcitatiCSVKod(UcitatiService):
    def naziv(self):
        return "Ucitati parser iz koda"
    def identifier(self):
        return "ucitati_parser_kod"

    def ucitati(self):
        return self._ubaci_csv()




    def _ubaci_csv(self):
        sampionati = {}
        timovi = {}
        term = ''
        file = open(apsolutnaPutanja("WorldCupMatches.csv"), "r")
        i = 0
        for line in file.readlines():
            if i==0:
                i = i+1
                continue
           ## if i == 10:
             ##   break
            i = i+1
            data = line.split(",")

            if data[0] not in sampionati:
                sampionati[data[0]] = Sampionat(data[0], [])
            if data[5] not in timovi:
                timovi[data[5]] = Tim(data[5])
            if data[8] not in timovi:
                timovi[data[8]] = Tim(data[8])
            utakmica = Utakmica(timovi[data[5]], timovi[data[8]], data[6]+":"+data[7])
            if "Group" in data[2]:
                if term in data[5] or term in data[8]:
                    if not data[7].isdigit() or not data[6].isdigit():
                        score = 0
                    else:
                        score = int(data[6]) + int(data[7])
                    ##if score >= int(filter):
                    sampionati[data[0]].dodajUtakmicu(utakmica, "Group", data[2])
            else:
                if term in data[5] or term in data[8]:
                    if not data[7].isdigit() or not data[6].isdigit():
                        score = 0
                    else:

                        score = int(data[6]) + int(data[7])
                ##    if score >= int(filter):
                    sampionati[data[0]].dodajUtakmicu(utakmica, data[2], data[2])

        return sampionati

