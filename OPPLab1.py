class BankAccount():
    def __init__(self,pin):
        self.pin = "pin"
        self.balance = 0
        self.pin = int(input(("please enter pin")))


    def deposit(self,pin,amount):
        if (amount >= 3000):
                pincheck = int(input(("please input pin to confirm")))
                if pincheck == self.pin:
                        self.balance = amount + self.balance
                        return self.balance
                else:
                        print("pin incorrect. Please try again!")
        else:
            self.balance = amount + self.balance
            print("balance has been updated. requested amount deposited")
            print("your new balance is",self.balance)
        return self.balance

    def withdraw(self,pin,amount):
            if (amount > self.balance):
                print('you cannot take out more then you have. please try again')
            else:
                self.balance = self.balance - amount
            print("balance has been updated. requested amount withdrawn")
            return self.balance

    def get_balance(self,pin):
        return self.balance

    def change_pin(self, old_pin, new_pin):
        self.pin = new_pin
        return self.pin

accountone=BankAccount(9872)

accounttwo=BankAccount(4378)


bankaccountdeposit = int(input(("how much would you like to deposit in account 1")))
accountone.deposit(9872,bankaccountdeposit)
bankaccountdeposittwo = int(input(("how much would you like to deposit in account 2")))
accounttwo.deposit(4378,bankaccountdeposittwo)

bankaccountwithdraw = int(input(("how much would you like to withdraw from account 1")))
accountone.withdraw(9872,bankaccountwithdraw)
bankaccountwithdrawtwo = int(input(("how much would you like to withdraw account 2")))
accounttwo.withdraw(4378,bankaccountwithdrawtwo)

print("current balance for account one",accountone.get_balance(9872))
print("current balance for account two",accounttwo.get_balance(4378))

newbankpin = int(input("enter your new bank pin please for account one"))
newbankpintwo = int(input("enter your new bank pin please for account two"))

print("new pin for account one is",accountone.change_pin(9872,newbankpin))
print("new pin for account two is",accounttwo.change_pin(4378,newbankpintwo))




