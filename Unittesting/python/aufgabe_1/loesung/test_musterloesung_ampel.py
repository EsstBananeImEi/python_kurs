import unittest

from Unittesting.python.aufgabe_1.loesung.ampel_loesung import Ampel


class TestMusterloesungAmpel(unittest.TestCase):
    def test__init__(self):
        ampel = Ampel(["a", "b", "c"], "a")

        assert ampel.liste_zustaende == ["a", "b", "c"]
        assert ampel.index_aktueller_zustand == 0

        ampel = Ampel(["a", "b", "c"], "b")
        assert ampel.liste_zustaende == ["a", "b", "c"]
        assert ampel.index_aktueller_zustand == 1

    def test_schalten(self):
        ampel = Ampel(["a", "b", "c"], "b")
        ampel.schalten()
        assert ampel.index_aktueller_zustand == 2

        ampel.schalten()
        assert ampel.index_aktueller_zustand == 0

    def test_get_zustand(self):
        ampel = Ampel(["a", "b", "c"], "b")
        rtv = ampel.get_zustand()
        assert rtv == "b"

    def test_set_zustand(self):
        ampel = Ampel(["a", "b", "c"], "a")
        ampel.set_zustand("c")
        assert ampel.index_aktueller_zustand == 2


if __name__ == "__main__":
    unittest.main()
