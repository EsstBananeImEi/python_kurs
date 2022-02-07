class Ampel(object):
    def __init__(self, liste_ampel_zustaende, anfangs_zustand):
        self.liste_zustaende = liste_ampel_zustaende
        self.index_aktueller_zustand = self.liste_zustaende.index(anfangs_zustand)

    def schalten(self):
        if self.index_aktueller_zustand < len(self.liste_zustaende) - 1:
            self.index_aktueller_zustand = self.index_aktueller_zustand + 1
        else:
            self.index_aktueller_zustand = 0

    def get_zustand(self):
        return self.liste_zustaende[self.index_aktueller_zustand]

    def set_zustand(self, zustand):
        self.index_aktueller_zustand = self.liste_zustaende.index(zustand)
