import json
import os

DATA_FILE = "accounts.json"

# --- Utility Functions ---
def load_accounts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_accounts(accounts):
    with open(DATA_FILE, "w") as f:
        json.dump(accounts, f, indent=4)

# --- ATM Class ---
class ATM:
    def __init__(self):
        self.accounts = load_accounts()

    def create_account(self):
        print("\n=== Create New Account ===")
        acc_num = input("Enter new Account Number: ")
        if acc_num in self.accounts:
            print("Account already exists!")
            return
        name = input("Enter your Name: ")
        pin = input("Set a 4-digit PIN: ")
        self.accounts[acc_num] = {"name": name, "pin": pin, "balance": 0}
        save_accounts(self.accounts)
        print(f"Account created successfully for {name}!")

    def login(self):
        print("\n=== Login ===")
        acc_num = input("Enter Account Number: ")
        pin = input("Enter PIN: ")

        account = self.accounts.get(acc_num)
        if account and account["pin"] == pin:
            print(f"Welcome {account['name']}!")
            self.account_menu(acc_num)
        else:
            print("Invalid account number or PIN.")

    def account_menu(self, acc_num):
        while True:
            print(f"\n=== {self.accounts[acc_num]['name']}'s Account ===")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                print(f"Balance: ₹{self.accounts[acc_num]['balance']}")
            elif choice == "2":
                amt = float(input("Enter amount to deposit: "))
                self.accounts[acc_num]['balance'] += amt
                save_accounts(self.accounts)
                print(f"Deposited ₹{amt}.")
            elif choice == "3":
                amt = float(input("Enter amount to withdraw: "))
                if amt <= self.accounts[acc_num]['balance']:
                    self.accounts[acc_num]['balance'] -= amt
                    save_accounts(self.accounts)
                    print(f"Withdrawn ₹{amt}.")
                else:
                    print("Insufficient balance!")
            elif choice == "4":
                print("Logging out...")
                break
            else:
                print("Invalid option, try again.")

# --- Main Program ---
def main():
    atm = ATM()
    while True:
        print("\n===== ATM MACHINE =====")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            atm.create_account()
        elif choice == "2":
            atm.login()
        elif choice == "3":
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
