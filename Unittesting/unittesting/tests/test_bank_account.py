import nose

from Unittesting.unittesting.code.bank_account import BankAccount


class TestBankAccount():

    def test__init__with_default(self):
        # Arrange
        # Act
        bank_account = BankAccount()
        # Assert
        assert bank_account.balance == 0

    def test__init__(self):
        # Arrange
        # Act
        bank_account = BankAccount(20)
        # Assert
        assert bank_account.balance == 20

    def test_deposit(self):
        # Arrange
        amount = 2
        expected_value = 22

        # Act
        bank_account = BankAccount(20)
        bank_account.deposit(amount)

        # Assert
        assert bank_account.balance == expected_value

    def test_withdraw(self):
        # Arrange
        amount = 8
        expected_value = 12

        # Act
        bank_account = BankAccount(20)
        bank_account.withdraw(amount)

        # Assert
        assert bank_account.balance == expected_value

    def test_withdraw_exception(self):
        # Arrange
        amount = 10

        # Act
        bank_account = BankAccount(9)

        # Assert
        with nose.tools.assert_raises(ValueError):
            bank_account.withdraw(amount)
