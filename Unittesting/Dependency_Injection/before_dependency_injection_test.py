import unittest
from unittest.mock import patch
from before_dependency_injection import *


class Verificator_Email_TestCase(unittest.TestCase):

    def test_init_verificator(self):
        verificator = Verificator_Email()
        self.assertFalse(verificator.is_verified())

    def test_verification_code_ascii(self):
        verificator = Verificator_Email()
        verificator._generate_verification_code()
        self.assertTrue(
            verificator._verification_code and verificator._verification_code.isascii())

    def test_verification_code_len(self):
        verificator = Verificator_Email()
        verificator._generate_verification_code()
        assert verificator._verification_code and len(
            verificator._verification_code) == 10

    def test_verify_success(self):
        verificator = Verificator_Email()
        verificator._generate_verification_code()
        with patch('builtins.input', return_value=verificator._verification_code):
            verificator.verify()
            self.assertTrue(verificator.is_verified())

    @patch('builtins.input', return_value="1234567")
    def test_verify_failed(self, mocked_input):
        verificator = Verificator_Email()
        verificator._generate_verification_code()
        verificator.verify()
        self.assertFalse(verificator.is_verified())


class LoginProcessor_TestCase(unittest.TestCase):

    def test_login_success(self):
        """ ? """
        self.assertTrue(True)

    def test_login_failed(self):
        """ ? """
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
