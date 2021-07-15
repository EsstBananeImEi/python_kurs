import nose
from mock import patch

from Unittesting.aufgabe.code.ampel import Ampel


class TestMusterloesungAmpel(object):

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
