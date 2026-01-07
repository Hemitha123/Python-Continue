class atm:
    def __init__(self,pin,balance):
        self.__pin=pin
        self.__balance=balance
        self.__authenticate=False      #atm is locked 
    def get_bal(self):
        return self.__balance
    def authenticate(self,pin):
        if self.__pin==pin:     #if authenticate passes only then it unlocks
            return "Authentication is successful"
        else:
            return "Authentication is Failed"
    def set_with(self,amount):
        if not self.__authenticate:     #if authenciation passes only then user can withdraw the amount
            return "please authenticate"
        if amount<=0:
            return "Invalid withdraw"
        else:
            self.__balance-=amount
c1=atm(1234,4000)
print(c1.get_bal())
print(c1.authenticate(6577))
c1.set_with(300)
print(c1.get_bal())