class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.checkings = BankAccount(int_rate=0.02, balance=0)
        self.savings = BankAccount(int_rate=0.02, balance=0)

    def transfer_money(self, amount, other_user):
        if other_user == person2:
            self.checkings.transfer(amount)
            person2.checkings.deposit(amount)
        elif other_user == person1:
            self.checkings.transfer(amount)
            person1.checkings.deposit(amount)
        else:
            print("please pick from Users")
            print("Person1 or Person2")
        return self

    def make_deposit(self, amount, account):
        if account == "Checkings":
            self.checkings.deposit(amount)
        elif account == "Savings":
            self.savings.deposit(amount)
        else:
            print("please pick from 1 account")
            print("Checkings or Savings")
        return self

    def make_withdrawal(self, amount, account):
        if account == "Checkings":
            self.checkings.withdraw(amount)
        elif account == "Savings":
            self.savings.withdraw(amount)
        else:
            print("please pick from 1 account")
            print("Checkings or Savings")
        return self

    def display_user_balance(self, account):
        if account == "Checkings":
            self.checkings.display_account_info()
        elif account == "Savings":
            self.savings.display_account_info()
        else:
            print("Please pick from 1 account")
            print("Checkings or Savings")
        return self

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
        print(f"Interest Rate: %{self.int_rate}")
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

    def transfer(self, amount):
        self.balance -= amount
        return self

    @classmethod
    def accounts_made(cls):
        print(f"{cls.accounts_counts} accounts in the program.")



person1 = User("Justin", "Justin@gmail.com")
person2 = User("Joe", "Joe@gmail.com")

person1.make_deposit(100, "Checkings").transfer_money(5, person2).display_user_balance("Checkings")
person2.make_deposit(200, "Checkings").transfer_money(10, person1).display_user_balance("Checkings")