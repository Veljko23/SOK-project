class Sampionat:
    def __init__(self, godina, faze):
        self.godina = godina
        self.faze = faze
    def dodajUtakmicu(self, utakmica, tip, naziv):
        faza = self.nadjiFazu(tip, naziv)
        if faza == None:
            faza = Faze(tip, naziv, [])
            self.faze.append(faza)
        ##print(len(self.faze))
        faza.dodajUtakmicu(utakmica)
    def nadjiFazu(self, tip, naziv):
        for faza in self.faze:
            if faza.tip == tip and faza.naziv == naziv:
                return faza
        return None
    def __str__(self):
        return self.godina

class Tim:
    def __init__(self, naziv):
        self.naziv = naziv
    def __str__(self):
        return self.naziv

class Utakmica:
    def __init__(self, domacin, gost, rezultat):
        self.domacin = domacin
        self.gost = gost
        self.rezultat = rezultat
    def __str__(self):
        return self.domacin

class Faze:
    def __init__(self, tip, naziv, utakmice):
        self.tip = tip
        self.naziv = naziv
        self.utakmice = utakmice
    def dodajUtakmicu(self, utakmica):
        self.utakmice.append(utakmica)
    def __str__(self):
        return self.tip

