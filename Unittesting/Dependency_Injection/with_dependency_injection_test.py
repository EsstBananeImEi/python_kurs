import unittest
from unittest.mock import patch
from with_dependency_injection import *


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

    def test_init(self):
        verificator = Verificator_Email()
        processor = LoginProcessor(verificator)
        self.assertEqual(processor.verificator, verificator)

    def test_login_success(self):
        verificator = Verificator_Email()
        verificator._generate_verification_code()
        with patch('builtins.input', return_value=verificator._verification_code):
            processor = LoginProcessor(verificator)
            user = User('$Melanie$')
            processor.login(user)
            self.assertEqual(user.get_status(), 'logged in')

    def test_login_failed(self):
        verificator = Verificator_Email()
        verificator._generate_verification_code()
        with patch('builtins.input', return_value='1234567890'):
            processor = LoginProcessor(verificator)
            user = User('$Melanie$')
            self.assertRaises(Exception, processor.login, user)


if __name__ == '__main__':
    unittest.main()
