class BankAccount:
    def __init__(self, account_number, account_last_name, account_first_name, account_balance,overdraft_allowed):
        self.__account_number = account_number
        self.__account_last_name = account_last_name
        self.__account_first_name = account_first_name
        self.__account_balance = account_balance
        self.__acount_overdraft = overdraft_allowed
        
    def get_account_number(self):
        return self.__account_number

    def get_account_last_name(self):
        return self.__account_last_name

    def get_account_first_name(self):
        return self.__account_first_name

    def get_account_balance(self):
        return self.__account_balance
    
    def get_account_overdraft(self):
        return self.__acount_overdraft
    
    def display_account_info(self):
        return (
            f"Account Number: {self.__account_number}\n"
            f"Account Holder: {self.__account_first_name} {self.__account_last_name}\n"
            f"Account Balance: ${self.__account_balance:.2f}"
        )
    
    def display_account_balance(self):
        return f"Account Balance: ${self.__account_balance:.2f}"
    
    def deposit_money(self, deposit_amount):
        if self.get_account_overdraft():
            self.__account_balance += deposit_amount
            return (
                f"You made a deposit of: ${deposit_amount}\n"
                f"Your account balance is now: ${self.__account_balance:.2f}"
                )
    
    def withdraw_money(self, withdraw_amount):
        if self.__account_balance - withdraw_amount < 0 and not self.__account_overdraft:
            return "Error: Insufficient funds and overdraft is not allowed."
        else:
            self.__account_balance -= withdraw_amount
            return (
                f"The amount you withdrew is: ${withdraw_amount}\n"
                f"Your account balance is now: ${self.__account_balance:.2f}"
                )
        
    def agios(self):
        if self.__account_balance < 0:
            fee = 10 
            self.__account_balance -= fee
            return f"A fee of ${fee} has been charged due to a negative balance."
        else:
            return "Your account balance is not negative."

    def transfer(self, recipient_account, amount):
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            recipient_account.__account_balance += amount
            return f"Transfer of ${amount} to account {recipient_account.get_account_number()} was successful."
        else:
            return "Insufficient funds for the transfer."

        
account_011 = BankAccount("101888", "Doe", "John", 2025.02, True)
account_022 = BankAccount("202999", "Smith", "Jane", -500.0, True)


# print(account_011.display_account_info())
# print(account_011.deposit_money(300))
# print(account_011.withdraw_money(2000))

print("\nInitial Account Balances:")
print(account_011.display_account_info())
print(account_022.display_account_info())

print("\nTransfer in progress")
print(account_011.transfer(account_022, 500))

print("\nUpdated Account Balances:")
print(account_011.display_account_balance())
print(account_022.display_account_balance())
