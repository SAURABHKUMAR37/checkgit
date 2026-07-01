class BankAccount:
    def __init__(self,accountn,own,balance):
        self.accountn=accountn
        self.own=own
        self.balance=balance
    def deposit(self,money):
        if(money>0):
            self.balance+=money
            print(f"after deposit balance{money} total is {self.balance}")
        else:
            print(" money does not deposit")
    def withdraw(self,money):
        if(money<=self.balance):
            self.balance-=money
            print("left balance is",self.balance)
        else:
            print("can not be withdraw")
    def check(self):
        print("current balance is",self.balance)
acn=BankAccount(123,"saurabh",5000)
acn.check()
acn.withdraw(1000)
acn.deposit(500)

    
