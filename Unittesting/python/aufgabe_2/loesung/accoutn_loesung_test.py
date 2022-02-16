import unittest
from datetime import datetime
from unittest.mock import patch
from account_loesung import Account, Membership, PaymentIntervall, PaymentMethod, User, Paypal


class MockedPayment(PaymentMethod):
    def validate_payment(self, payment_data: bool) -> bool:
        return True

    def pay(self, amount: float) -> None:
        pass


class MockedMembership(Membership):
    def get_fee(self) -> float:
        return 10.0


class MockedPaymentIntervall(PaymentIntervall):
    def payment_intervall_in_months(self) -> int:
        return 12


class TestAccount(unittest.TestCase):
    def test_init(self):
        test_user = User("$user$", 12)
        account = Account(
            test_user, 1, MockedPaymentIntervall(), MockedMembership())
        self.assertEqual(account.current_date, datetime.now())

    def test_check_payment_intervall_True(self):
        test_user = User("$user$", 12)
        account = Account(
            test_user, 1, MockedPaymentIntervall(), MockedMembership())
        account.last_payment = datetime(2022, 1, 1)
        account.current_date = datetime(2023, 1, 1)
        rtv = account.check_payment_intervall()
        self.assertTrue(rtv)

    def test_check_payment_intervall_False(self):
        test_user = User("$user$", 12)
        account = Account(
            test_user, 1, MockedPaymentIntervall(), MockedMembership())
        account.last_payment = datetime(2022, 1, 1)
        account.current_date = datetime(2022, 12, 31)
        rtv = account.check_payment_intervall()
        self.assertFalse(rtv)

    def test_initialize_payment_successful(self):
        test_user = User("$user$", 12)
        account = Account(
            test_user, 1, MockedPaymentIntervall(), MockedMembership())
        account.last_payment = datetime(2021, 1, 1)

        with patch.object(Account, "check_payment_intervall", return_value=True):
            rtv = account.initialize_payment(Paypal())
            self.assertEqual(
                rtv,  f"payment on {account.current_date} successful")

    def test_initialize_payment_not_successful(self):
        test_user = User("$user$", 12)
        account = Account(
            test_user, 1, MockedPaymentIntervall(), MockedMembership())
        account.last_payment = datetime(2021, 1, 1)

        with patch.object(Account, "check_payment_intervall", return_value=True), \
                patch.object(Paypal, "validate_payment", return_value=False):
            rtv = account.initialize_payment(Paypal())
            self.assertEqual(
                rtv,  f"payment not successful")

    def test_initialize_payment_not_have_to_pay(self):
        test_user = User("$user$", 12)
        account = Account(
            test_user, 1, MockedPaymentIntervall(), MockedMembership())
        account.last_payment = datetime(2021, 1, 1)

        with patch.object(Account, "check_payment_intervall", return_value=False):
            rtv = account.initialize_payment(Paypal())
            self.assertEqual(
                rtv,  f"{account.user.name} does not have to pay yet")


if __name__ == "__main__":
    unittest.main()
