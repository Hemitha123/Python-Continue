#Banking System Simulation

class account():
    def __init__(self,balance):     #initialization
        self.balance=balance
    def  cal_int(self):
        print("Interest are")

class savingsAccount(account):
    def cal_int(self):
        int_s=self.balance*0.05     #calculates the interest
        print(f"The interest for SavingsAccount is {int_s} ")
class currentAccount(account):
    def cal_int(self):
        int_c=self.balance*0.02     #calculates the interest
        print(f"The interest for CurrentAccount is {int_c}")
class fixedDeposit(account):
    def cal_int(self):
        int_f=self.balance*0.08     #calculates the interest
        print(f"The interest for FixedDeposit is {int_f}")

Account=account(10000)
SavingsAccount=savingsAccount(10000)
CurrentAccount=currentAccount(10000)
FixedDeposit=fixedDeposit(10000)

for x in (SavingsAccount,CurrentAccount,FixedDeposit):
    x.cal_int()