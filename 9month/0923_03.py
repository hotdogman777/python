# 추상 클래스 Payment를 정의하고, pay(amount)를 추상 메서드로 선언하세요
from abc import ABC, abstractclassmethod


class Payment(ABC):
    @abstractclassmethod
    def pay(self, amount):
        pass
# CardPayment 클래스와 CashPayment 클래스는 Payment를 상속받아 pay() 메서드를 오버라이딩 하세요
    # CardPayment: 카드로 {amount}원을 결제합니다.
    # CashPayment: 현금으로 {amount}원을 결제합니다.


class CardPayment(Payment):
    def pay(self, amount):
        print(f"CardPayment: 카드로 {amount}원을 결제합니다.")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"CashPayment: 현금으로 {amount}원을 결제합니다.")


cash_pay = CashPayment()
card_pay = CardPayment()
card_pay.pay(20000)
cash_pay.pay(20000)
