# Payment System
# This program demonstrates abstraction and polymorphism.

from abc import ABC, abstractmethod


# Abstract class
class Payment(ABC):

    @abstractmethod
    def makePayment(self):
        pass


# Mobile Money payment class
class MobileMoneyPayment(Payment):

    def makePayment(self):
        print("Payment made using Mobile Money")


# Bank Card payment class
class CardPayment(Payment):

    def makePayment(self):
        print("Payment made using Bank Card")


# Main section

mobile_payment = MobileMoneyPayment()
card_payment = CardPayment()

# Make payments
mobile_payment.makePayment()
card_payment.makePayment()
