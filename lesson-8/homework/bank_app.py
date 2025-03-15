import os
import json

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if self.balance >= amount > 0:
            self.balance -= amount
            return f"Withdrawn ${amount}. New balance: ${self.balance}"
        return "No sufficient balance."

    def to_dic(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}

    def __str__(self):
        return f"Account: {self.account_number} \nName: {self.name} \nBalance: {self.balance}"

class Bank:
    def __init__(self, filename = "accounts.txt"):
        self.accounts = {}
        self.filename = filename
        self.load_from_file()

    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                try:
                    data = json.load(file)
                    self.accounts = {acc: Account(**data[acc]) for acc in data}
                except json.JSONDecodeError:
                    self.accounts = {}

    def save_to_file(self):
        with open(self.filename, "w") as file:
            json.dump({acc: self.accounts[acc].to_dic() for acc in self.accounts}, file)

    def create_account(self, name, initial_deposit):
        account_number = str(len(self.accounts) + 1001)
        if initial_deposit < 0:
            return "Initial deposit must be non-negative."

        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        return f"Account created successfully. Account number: {account_number}"

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account
        else:
            return "Account not found."

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if amount > 0:
            result = account.deposit(amount)
            self.save_to_file()
            return result
        else:
            return "Account not found."

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            result = account.withdraw(amount)
            self.save_to_file()
            return result
        else:
            return "Account not found."


if __name__ == "__main__":
    bank = Bank()

    while True:
        print("\nBank Application")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            deposit = float(input("Enter initial deposit: "))
            print(bank.create_account(name, deposit))
        elif choice == "2":
            acc_num = input("Enter account number: ")
            print(bank.view_account(acc_num))
        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            print(bank.deposit(acc_num, amount))
        elif choice == "4":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            print(bank.withdraw(acc_num, amount))
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")