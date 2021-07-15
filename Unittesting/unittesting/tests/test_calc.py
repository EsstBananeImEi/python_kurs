import nose
from mock import patch

from Unittesting.unittesting.code.calculator import Calc


class TestCalc(object):

    def test_sum_list(self):
        # Arrange
        calc = Calc()
        liste = [1, 2, 3]

        # Act
        rtv = calc.sum_list(liste)

        # Assert
        assert rtv == 6

    def test_addiere(self):
        # Arrange
        calc = Calc()
        number_1 = 5
        number_2 = 6

        # Act
        rtv = calc.addiere(number_1, number_2)

        # Assert
        assert rtv == 11

    def test_subtrahieren(self):
        # Arrange
        calc = Calc()
        number_1 = 10
        number_2 = 6

        # Act
        rtv = calc.subtrahieren(number_1, number_2)

        # Assert
        assert rtv == 4

    def test_multiplizieren(self):
        # Arrange
        calc = Calc()

        # Act
        # Assert
        assert calc.multiplizieren(10, 6) == 60
        assert calc.multiplizieren(4, 2.5) == 10
        assert calc.multiplizieren(10, 0) == 0

    def test_dividieren(self):
        # Arrange
        calc = Calc()
        number_1 = 5
        number_2 = 2

        # Act
        rtv = calc.dividieren(number_1, number_2)

        # Assert
        assert rtv == 2.5
