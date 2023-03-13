class BankAccount:

    accounts_counts = 0

    def __init__(self, int_rate=0.002, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts_counts += 1

    def deposit(self, amount):
        print(f"Current Balance: ${self.balance}")
        print(f"Deposited: ${amount}")
        self.balance += amount
        print(f"New Balance: ${self.balance}")
        print("")
        return self
    
    def withdraw(self, amount):
        print(f"Current Balance: ${self.balance}")
        self.balance -= amount
        if self.balance < 0:
            self.balance += amount - 5
            print("Insufficient funds: Charging a $5 fee.")
            print(f"Balance: ${self.balance}")
            print("")
        else:
            print(f"Withdrawal: ${amount}")
            print(f"New Balance: ${self.balance}")
            print("")
        return self

    def display_account_info(self):
        print(f"Interest Rate: {self.int_rate}")
        print(f"Account Balance: ${self.balance}")
        print("")
        return self

    def yield_interest(self):
        if self.balance >= 0:
            print(f"Current Balance: ${self.balance}")
            int_amount = self.balance * self.int_rate
            self.balance += int_amount
            print(f"% {self.int_rate} added to balance.")
            print(f"New Balance: {self.balance}")
            print("")
            return self
        else:
            return

    @classmethod
    def accounts_made(cls):
        print(f"{cls.accounts_counts} accounts in the program.")

account1 = BankAccount(0.002, 0)
account2 = BankAccount(0.004, 0)

account1.deposit(50).deposit(25).deposit(25).withdraw(10).yield_interest().display_account_info()
account2.deposit(200).deposit(20).withdraw(30).withdraw(15).withdraw(70).withdraw(35).yield_interest().display_account_info()

BankAccount.accounts_made()
