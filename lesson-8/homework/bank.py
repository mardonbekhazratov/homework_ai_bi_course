
class Bank:

    def __init__(self):
        self.accounts = dict()
        self.count = 0
        self.file_name = "accounts.txt"
    
    def create_account(self, name, initial_deposit):
        if not isinstance(name, str):
            raise ValueError("Name must be string!")
        
        if not isinstance(initial_deposit, (int,float)):
            raise ValueError("Initial deposit must be a number!")
        
        self.count += 1
        account_number = self.count
        self.accounts[account_number] = Account(account_number, name, initial_deposit)

        self.save_to_file(self.accounts[account_number])


    def view_account(self, account_number):
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer!")
        
        return self.accounts[account_number]
    

    def deposit(self, account_number, amount):
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer!")
        
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number!")
        
        self.accounts[account_number].balance += amount

        self.save_to_file(self.account[account_number])


    def withdraw(self, account_number, amount):
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer!")
        
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number!")
        
        if amount > self.accounts[account_number].balance:
            raise ValueError("Amount must be less than or equal to account balance!")
        
        self.accounts[account_number].balance -= amount

        self.save_to_file(self.accounts[account_number])


    def save_to_file(self, acc):
        accounts = self.load_from_file
        with open(self.file_name, "w") as file:
            found = False
            for account in accounts:
                account = account.split(", ")
                if account[0] == str(acc.account_number):
                    found = True
                    account[1] = acc.name
                    account[2] = acc.balance
                file.write(", ".join(account) + "\n")
            if not found:
                file.write(str(acc.account_number) + ", " + acc.name + ", " + str(acc.balance) + "\n")


    @property
    def load_from_file(self):
        try:
            with open(self.file_name, "r"):
                pass
        except:
            with open(self.file_name, "w"):
                pass
        with open(self.file_name, "r") as file:
            lines = file.readlines()
        return lines


class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance


    def __str__(self):
        return self.name + " " + self.balance

