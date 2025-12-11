 #Single Inheritance

class account():
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"The amount {amount} is added to the balance")
    def display(self):
       print(f"The Account Holder name is {self.name}")
       print(f"Current balance is {self.balance}")
    
class savingsAcc(account):
    def __init__(self,name,balance,interest_rate):
        super().__init__(name,balance)
        self.interest_rate=interest_rate

    def calculate_interest(self,years):
       si=(self.balance*self.interest_rate*years)/100
       print(f"Simple interest for {years} years is {si}")

a1=savingsAcc("amar",30000,5)
a1.deposit(3000)
a1.display()
a1.calculate_interest(2)

