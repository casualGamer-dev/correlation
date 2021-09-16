class Atm(object):
    def __init__(self,pin,amount):
        self.pin = pin
        self.amount=amount
        self.BankBalance=1000
    def withdraw(self,amount):
          pin=int(input("enter your pin"))
          if pin == self.pin:
           WithdrawAmount=self.amount
           finalBalance=self.BankBalance-WithdrawAmount
           self.BankBalance=finalBalance
    def BalanceCheck(self):
         pin=int(input("enter your pin"))
         if pin == self.pin:
              print(self.BankBalance)
         else:
             print("please enter the correct pin")
def main():
    e=input("please select what you want to do   withdraw or check balance   ")
    atm= Atm(1234,0)
    if e == "withdraw":
        amount=int(input("input the amount of money you want"))
        atm.withdraw(amount)
    else:
        atm.BalanceCheck()
main()