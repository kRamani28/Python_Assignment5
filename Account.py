# 4.Implement a Banking account

class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate
account1 = SavingsAccount("Ashish", 5000, 5)
print(account1.title)
print(account1.balance)
print(account1.interestRate)

# output #Ashish is the title,5000 is the balance and 5 is the interesrRate
# Ashish
#5000
#5



 


