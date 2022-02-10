from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Membership(ABC):
    @abstractmethod
    def get_fee(self) -> float:
        raise NotImplementedError


class BronzeMembership(Membership):
    def get_fee(self) -> float:
        return 20.0


class SilverMembership(Membership):
    def get_fee(self) -> float:
        return 60.0


class GoldMembership(Membership):
    def get_fee(self) -> float:
        return 80.0


@dataclass
class User:
    name: str
    age: int
    """and many more variables and methods"""


@dataclass
class PaymentIntervall(ABC):
    @abstractmethod
    def payment_intervall_in_months(self) -> int:
        raise NotImplementedError

    def diff_month(self, date_now: datetime, date_then: datetime) -> int:
        return (date_now.year - date_then.year) * 12 + date_now.month - date_then.month


class MonthlyPayment(PaymentIntervall):
    def payment_intervall_in_months(self) -> int:
        return 1


class SemiannualPayment(PaymentIntervall):
    def payment_intervall_in_months(self) -> int:
        return 6


class YearlyPayment(PaymentIntervall):
    def payment_intervall_in_months(self) -> int:
        return 12


class PaymentMethod(ABC):
    @abstractmethod
    def validate_payment(self, payment_data: bool) -> bool:
        raise NotImplementedError

    @abstractmethod
    def pay(self, amount: float) -> None:
        raise NotImplementedError


class Paypal(PaymentMethod):
    def validate_payment(self, payment_data: bool) -> bool:
        """
        Only for demonstration
        returns the parameter
        return must be manipulated in the tests
        """
        return payment_data

    def pay(self, amount: float) -> None:
        """Does a lot of Payment stuff"""


@dataclass
class Account:
    def __init__(
        self,
        user: User,
        id: int,
        payment_intervall: PaymentIntervall,
        membership: Membership,
    ) -> None:
        self.user = user
        self.id = id
        self.last_payment = datetime(2022, 2, 1)
        self.payment_intervall = payment_intervall
        self.membership = membership
        self.current_date = datetime.now()

    def check_payment_intervall(self) -> bool:
        time_past = self.payment_intervall.diff_month(
            self.current_date, self.last_payment
        )
        if time_past >= self.payment_intervall.payment_intervall_in_months():
            return True
        return False

    def initialize_payment(self, payment_service: PaymentMethod) -> str:
        if not self.check_payment_intervall():
            return f"{self.user.name} does not have to pay yet"

        amount = (
            self.payment_intervall.payment_intervall_in_months()
            * self.membership.get_fee()
        )
        if payment_service.validate_payment(True):
            payment_service.pay(amount)
            return f"payment on {self.current_date} successful"
        return "payment not successful"
