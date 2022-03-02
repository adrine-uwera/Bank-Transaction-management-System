# File for Account (parent class)

# Account class which other types of account will inherit from.

from datetime import datetime   # imports the datetime class from datetime module in python
from W7_A3_Q1_Adrine_Uwera_client import Client       # imports Client class from client file
dangote_account_records = []    # an array to store data for Dangote bank including client and account information


class Account(Client):          # a class named Account which inherited Client class
    # inherited Client class because account holders information is a part of in account details

    next_account_number = 100000    # a variable for account_number
    # when a client opens an account he/she will be given an account number automatically
    # this will avoid having accounts with same account number

    def __init__(self, name, age, gender, occupation):      # initialize account properties
        super().__init__(name, age, gender, occupation)     # gives access to Client (parent class) properties
        self.date_created = datetime.now()                  # records the date on which the account is created
        self.account_balance = 0                            # keep track of the balance on the account and
        # initialized at zero because when an account is created there is no money on the account

        self.account_number = Account.next_account_number   # assigns account number to the account created
        Account.next_account_number += 1              # increments the account number when the previous number is taken
        dangote_account_records.append(self)          # adds the account details to the dangote_account_records array

    def __str__(self):          # display account details in an organized structure
        print(" \nAccount details:\n--------------- ")
        # the str() function converts the properties to strings so as to allow concatenation
        details = "Account holder's name: " + str(self.name) + "\n"
        details += "Account holder's age: " + str(self.age) + "\n"
        details += "Account holder's gender: " + str(self.gender) + "\n"
        details += "Account holder's occupation: " + str(self.occupation) + "\n"
        details += "Account number: " + str(self.account_number) + "\n"
        details += "Account's date created: " + str(self.date_created) + "\n"
        details += "Account balance: " + "$" + str(self.account_balance) + "\n"
        return details      # return all the account details

    def view_account_balance(self):     # a method to display account balance
        print("\nCurrent balance")
        print("---------------")

        # displays the account balance at the moment
        print(f"Account number: {self.account_number} \nAccount balance: ${self.account_balance}\n")

    def deposit_money(self, money_deposited):    # a method to deposit money in the bank account
        date_deposited = datetime.now()          # records the date when the money was deposited
        self.account_balance += money_deposited     # updates the balance by adding the money deposited
        print(f"The money was successfully deposited.\n")   # displays to indicate that the deposit was done
        print(f"Date deposited: {date_deposited}")      # displays the date when the money was deposited
        self.view_account_balance()     # displays the account balance after depositing money

    def withdraw_money(self, money_withdrawn):       # a method to withdraw money from the bank account
        if money_withdrawn <= self.account_balance:  # checks if the sender has sufficient money to withdraw
            self.account_balance -= money_withdrawn     # updates the balance by removing the money withdrawn
            print(f"The money was successfully withdrawn.\n")   # displays to indicate that the withdraw was done
            date_withdrawn = datetime.now()         # records the date when the money was withdrawn
            print(f"Date withdrawn: {date_withdrawn}")  # displays the date when the money was withdrawn
            self.view_account_balance()     # displays the account balance after withdrawing money
        else:
            # displays a message to tell the user that they have insufficient money on their account and show balance
            print(f"There is no enough money on the account. \nAccount balance: ${self.account_balance}")

    def transfer_money(self):  # method to transfer money between client's accounts
        try:
            money_transferred = float(input("Enter the amount to transfer in numerical form: $"))   # asks the amount of money to be transferred
            if money_transferred <= self.account_balance:   # checks if the sender has sufficient money to transfer
                acc_nbr5 = int(input("Enter account number of the receiver account: "))  # asks user input for receiver account number
                for receiver_account in dangote_account_records:    # loops through the list of accounts
                    if acc_nbr5 == receiver_account.account_number:     # checks if the receiver account an account under dangote bank
                        self.account_balance -= money_transferred   # updates the balance by removing the money transferred
                        receiver_account.account_balance += money_transferred   # updates the balance by adding the money transferred
                        print("The money was transferred successfully.\n")  # message to indicate that the transfer was done
                        date_transferred = datetime.now()  # records the date when the money was transferred
                        print(f"Date transferred: {date_transferred}")  # displays the date when the money was transferred

                        # displays the account balance for both sender and receiver's accounts after the transfer
                        print(f"Sender's account balance: ${self.account_balance} "
                              f"\nReceiver's account balance: ${receiver_account.account_balance}\n")
                        break
                else:  # displays to tell the user that the account entered is not found hence transaction failed
                    print("Transaction failed!")
                    print("\nAccount referred to does not exist under Dangote bank."
                          "\nPlease verify the account number entered and try again\n")
            else:
                # displays a message to tell the user that they have insufficient money on their account and show balance
                print("\nTransaction failed!")
                print(f"There is no enough money on the account. \nAccount balance: ${self.account_balance}\n")

        except ValueError:  # displayed when the user's input type is invalid
            print('ONLY NUMBER ARE ALLOWED!!!!')
