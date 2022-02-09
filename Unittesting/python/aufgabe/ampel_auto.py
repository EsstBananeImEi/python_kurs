from ampel import Ampel


class AmpelAuto(Ampel):
    def __init__(self, anfangs_zustand: str):
        super().__init__(["Rot", "Rotgelb", "Grün", "Gelb"], anfangs_zustand)

    def get_lampen(self) -> tuple[bool, bool, bool]:
        lampen = (False, False, False)
        zustand = self.liste_zustaende[self.index_aktueller_zustand]
        if zustand == "Rot":
            lampen = (True, False, False)
        elif zustand == "Rotgelb":
            lampen = (True, True, False)
        elif zustand == "Grün":
            lampen = (False, False, True)
        elif zustand == "Gelb":
            lampen = (False, True, False)
        return lampen


if __name__ == "__main__":
    a = AmpelAuto("Rot")
    print(a.get_zustand())
    print(a.get_lampen())
    print()
    for i in range(2):
        a.schalten()
        print(a.get_zustand())
        print(a.get_lampen())
        print()
