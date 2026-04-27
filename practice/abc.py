from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class CreditCard(Payment):
    def pay(self,amount):
        print(f"paid amount {amount} using credit card.")

class UPI(Payment):
    def pay(self,amount):
        print(f"paid amount {amount} using UPI.")

p1=CreditCard()
p2=UPI()
p1.pay(1000)
p2.pay(500)

