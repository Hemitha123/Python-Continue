class bankaccount:
    def __init__(self,balance,acc_number):
        self.__balance=balance
        self.__acc_number=acc_number
    def get_bal(self):
        return self.__balance
    def get_accnum(self):
        return self.__acc_number
    def set_dep(self,amount):       #if the amount is greater than 0 then adds to balance
        if amount>0:
            self.__balance=self.__balance+amount
        else:
            return "No negative deposits"
    def set_with(self,amount):
        if amount>self.__balance:   #amount cannot withdreaw more than the balance
            return "No Overdrafts"
        elif amount<=0:
            return "Invalid withdraw"
        else:
            self.__balance-=amount
c1=bankaccount(5000,123)
print(f"Account Balance:{c1.get_bal()}")
print(f"Account number:{c1.get_accnum()}")

c1.set_dep(1000)
print(f"Account Balance after deposit:{c1.get_bal()}")
c1.set_with(200)
print(f"Account Balance after withdraw:{c1.get_bal()}")
