#1- Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality.

class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        # Private attributes with double underscores to enforce encapsulation
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
            amount (float): The amount to deposit.

        Returns:
            None
        """
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            None
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        elif amount > self.__account_balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")

    def display_balance(self):
        """
        Display the account balance.

        Returns:
            None
        """
        print(f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}")


# Create an instance of the BankAccount class
account = BankAccount("1234567890", "John Doe", 1000)

# Test deposit functionality
account.deposit(500)

# Test withdrawal functionality
account.withdraw(200)

# Display the account balance
account.display_balance()
