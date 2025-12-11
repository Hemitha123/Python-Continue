class bankaccount():
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance      #variables are initialized
    def deposite(self,amount):
        if amount>0:    #if amount is greater than 0 then it enters the loop
            self.balance+=amount    #and gets added to the balance
            print(f"The amount {amount} is added to the account holder {self.account_holder}")
            print(f"The balance amount after deposite is:{self.balance}")

    def withdrawal(self,amount):
        if amount>self.balance:  #if amount is greater than balance 
            print(f"Insufficent Balance amount:{self.balance}for withdrawal")
        else:
            self.balance-=amount  #else it get subtracted
            print(f"The current balance after withdrawal is:{self.balance}")
    def check_balance(self):   #checks the balance
        print(f"The balance amount is:{self.balance}")

account1=bankaccount("Amar",20000)
account2=bankaccount("Riya",30000)

account1.deposite(4000)
account1.withdrawal(3000)
account1.check_balance()

account2.deposite(1000)
account2.withdrawal(2000)
account2.check_balance()

