from ampel import Ampel


class AmpelAuto(Ampel):
    def __init__(self, anfangs_zustand: str):
        super().__init__(["Rot", "Rotgelb", "Grün", "Gelb"], anfangs_zustand)

    def get_lampen(self) -> tuple[bool, bool, bool]:
        zustand = self.liste_zustaende[self.index_aktueller_zustand]
        match zustand:
            case "Rot": return  (True, False, False)
            case "Rotgelb": return  (True, True, False)
            case "Gelb": return  (False, True, False)
            case "Grün": return  (False, False, True)
            case _ : return (False, False, False)  


if __name__ == "__main__":
    a = AmpelAuto("Rot")
    for i in range(2):
        a.schalten()
        print(a.get_zustand())
        print(a.get_lampen())
        print()
