class BankAccount:
    balance = 1000

    def set_balance(self,balance):
        self.balance = balance

    def withdrow(self,amount):
        if amount > self.balance:
            print("Your balance is less then you want. Balance is {}".format(self.balance))
        else:
            self.set_balance(self.balance - amount)
            print("Your balance now is {}".format(self.balance))

    def deposit(self):
        print("this is deposit {}".format(self.balance))

class PremiumBankAccount(BankAccount): #(please implement constructor with super call )
    creditthreshold = 5000 # credit_threshold more pythonic , and if it constant use capital case CREDIT_TRESHOLD

    def set_creditthreshold(self,creditthreshold): # if creditthreshold common for all class instances, you can
        self.creditthreshold = creditthreshold     # use class creditthreshold constant

    def withdrow(self,amount):
        if amount > self.creditthreshold: # what if person have money on balance ?
            print("Your Creditthreshold is less then you want. Creditthreshold is {}".format(self.creditthreshold))
        else:
            self.set_creditthreshold((self.creditthreshold - amount)) # why you get money only from credit ?
            print("""Because of you are premium account you can get more thaen you have on current balance.
Current Credit Balance is: {}""".format(self.creditthreshold))


class Persone():
    salarytrashold = 3000

    def __init__(self,f_name,l_name,salary):
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary

    def set_salarytrashold(self,salarytrashold):
        self.salarytrashold = salarytrashold

    def change_salary(self,new_selary):
        self.salary = new_selary # if Person salary changes, it don't change bank account type :(

    def bank_account(self):
        print("""FirstName: {0}
LastName: {1}""".format(self.f_name,self.l_name))
        if self.salary > self.salarytrashold:
            print("{0} {1}`S BANK ACCOUNT IS PREMIUM".format(self.f_name,self.l_name))
            return PremiumBankAccount()
        else:
            print("{0} {1}`S BANK ACCOUNT IS NOT PREMIUM".format(self.f_name, self.l_name))
            return BankAccount()

a = Persone("Arman","Baghajyan",5000)
a.bank_account().withdrow(200)


