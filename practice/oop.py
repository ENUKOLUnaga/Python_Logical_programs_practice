class Bank:
    def __init__(self):
        self.__balance=1000
    
    def deposit(self,amount):
        self.__balance+=amount
    
    def get_balance(self):
        return self.__balance
    
b1=Bank()
b1.deposit(100)
print(b1.get_balance())
b1.deposit(100)
print(b1.get_balance())
b2=Bank()
b2.deposit(200)
print(b2.get_balance())
