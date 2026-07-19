# 2: Write a Python program to implement a class named BankAccount with the following requirements:
# The class should contain two instance variables:
# Name (Account holder name)
# Amount (Account balance)
# The class should contain one class variable:
# ROI (Rate of Interest), initialized to 10.5
# Define a constructor (__init__) that accepts Name and initial Amount.
# Implement the following instance methods:
# Display () - displays account holder name and current balance
# Deposit () - accepts an amount from the user and adds it to balance
# Withdraw() - accepts an amount from the user and subtracts it from balance
# (Ensure withdrawal is allowed only if sufficient balance exists)
# CalculateInterest () - calculates and returns interest using formula:
# Interest = (Amount * ROI) / 100
# Create multiple objects and demonstrate all methods.

class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("\nAccount Holder : ", self.Name)
        print("Balance : ", self.Amount)

    def Deposit(self):
        deposit = float(input("Enter amount to deposit: "))
        self.Amount += deposit
        print("Amount deposited successfully.")

    def Withdraw(self):
        withdraw = float(input("Enter amount to withdraw: "))

        if withdraw <= self.Amount:
            self.Amount -= withdraw
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    # Calculate interest
    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest

obj1 = BankAccount("Mickey Mouse", 50000)
obj2 = BankAccount("Donald Duck", 30000)

print("----- Account 1 -----")
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.Display()
print("Interest :", obj1.CalculateInterest())

print("\n----- Account 2 -----")
obj2.Display()
obj2.Deposit()
obj2.Withdraw()
obj2.Display()
print("Interest :", obj2.CalculateInterest())

#OUTPUT
# ----- Account 1 -----

# Account Holder :  Mickey Mouse
# Balance :  50000
# Enter amount to deposit: 500
# Amount deposited successfully.
# Enter amount to withdraw: 350
# Amount withdrawn successfully.

# Account Holder :  Mickey Mouse
# Balance :  50150.0
# Interest : 5265.75

# ----- Account 2 -----

# Account Holder :  Donald Duck
# Balance :  30000
# Enter amount to deposit: 4000
# Amount deposited successfully.
# Enter amount to withdraw: 2300
# Amount withdrawn successfully.

# Account Holder :  Donald Duck
# Balance :  31700.0
# Interest : 3328.5