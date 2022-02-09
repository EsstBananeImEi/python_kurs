import unittest

from ampel_auto import AmpelAuto


class TestMusterloesungAmpelAuto(unittest.TestCase):
    def test__init__(self):
        auto_ampel = AmpelAuto("Rot")
        assert auto_ampel.index_aktueller_zustand == 0

    def test_get_lampen_rot(self):
        auto_ampel = AmpelAuto("Rot")
        rot, gelb, gruen = auto_ampel.get_lampen()

        assert rot is True
        assert gelb is False
        assert gruen is False

    def test_get_lampen_gruen(self):
        auto_ampel = AmpelAuto("Grün")
        rot, gelb, gruen = auto_ampel.get_lampen()

        assert rot is False
        assert gelb is False
        assert gruen is True

    def test_get_lampen_gelb(self):
        auto_ampel = AmpelAuto("Gelb")
        rot, gelb, gruen = auto_ampel.get_lampen()

        assert rot is False
        assert gelb is True
        assert gruen is False

    def test_get_lampen_rotgelb(self):
        auto_ampel = AmpelAuto("Rotgelb")
        rot, gelb, gruen = auto_ampel.get_lampen()

        assert rot is True
        assert gelb is True
        assert gruen is False


if __name__ == "__main__":
    unittest.main()
