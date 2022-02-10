import unittest
from datetime import datetime

from account_loesung import Account, Membership, PaymentIntervall, PaymentMethod, User


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
        account = Account(test_user, 1, MockedPaymentIntervall(), MockedMembership())
        self.assertEqual(account.current_date, datetime.now())


if __name__ == "__main__":
    unittest.main()
