# File for Savings Account (child class)

from W7_A3_Q1_Adrine_Uwera_class_account import dangote_account_records   # imports the array containing all account details
import W7_A3_Q3_Adrine_Uwera_current_account      # imports current account file  as whole because all codes in the file are needed
from datetime import datetime  # imports the datetime class from datetime module in python


class SavingsAccount(W7_A3_Q3_Adrine_Uwera_current_account.CurrentAccount):    # a class named CurrentAccount which inherited Client class
    # inherited CurrentAccount class from current_account file because all other functionalities of a savings account
    # are the same as those of a current account is an account except a few modification.

    interest_rate = 0.03  # variable for the interest earn by a client when his/her money stays in the bank for a month
    # 0.03 is equivalent to 3%
    # This interest rate will replace the interest rate in the inherited class

    # a method for withdrawing from the client's account after the respective period
    # This method overrides the withdraw_money in the parent class
    def withdraw_money(self, money_withdrawn):

        # variable that takes in user input to specify the period the money has been in the bank
        period = float(input("For how many months has the money been in the bank since your last withdraw?"
                             "\nEnter the number of months in figures: "))

        # a variable for 6 month period that the money must stay in the bank in order for the user
        # to be allowed to withdraw money from the bank account
        no_withdraw_period = 6

        # round the number down to the nearest integer in case the user enters an decimal number
        # decimal number means that the month would have been in the bank for n months and some days
        # the number is round down to the nearest integer because the decimals after the whole number of month
        # are not a complete month so the client won't withdraw until after 6 complete months.
        # additionally there was no need to import the math library again since we had it in the current_account file
        period = W7_A3_Q3_Adrine_Uwera_current_account.math.floor(period)

        # checks the period the money has been in the bank is greater than or equal 6 month
        if period >= no_withdraw_period:

            if money_withdrawn <= self.account_balance:  # checks if the account has sufficient money to withdraw
                self.account_balance -= money_withdrawn  # updates the balance by removing the money withdrawn
                date_withdrawn = datetime.now()  # records the date when the money was withdrawn
                print(f"Date withdrawn: {date_withdrawn}")  # displays the date when the money was withdrawn
                self.view_account_balance()  # displays the account balance after withdrawing money
                return "Successful"

            else:
                # displays a message to tell the user that they have insufficient money on their account
                # and show balance
                print(f"There is no enough money on the account. \nAccount balance: ${self.account_balance}")
        else:
            # displays a message to tell the user that the 6 month period is not yet over
            print("Insufficient period. You are only allowed to withdraw money after a period of 6 months.\n")

    # method to transfer money between client's accounts
    # This method overrides the transfer_money in the parent class
    def transfer_money(self):
        try:
            money_transferred = float(input("Enter the amount to transfer in numerical form: $"))   # asks the amount of money to be transferred
            if money_transferred <= self.account_balance:   # checks if the sender has sufficient money to transfer
                acc_nbr5 = int(input("Enter account number of the receiver account: "))     # asks user input for receiver account number
                for receiver_account in dangote_account_records:        # loops through the list of accounts
                    if acc_nbr5 == receiver_account.account_number:     # checks if the receiver account is under dangote bank
                        if self.withdraw_money(money_transferred) == "Successful":      # checks if the withdraw was successful considering that the saving account holders are allowed to withdraw only after 6 months
                            receiver_account.account_balance += money_transferred   # updates the balance by adding the money transferred
                            print("\nThe money was transferred successfully.\n")  # message to indicate that the transfer was done

                            # displays the account balance for both sender and receiver's accounts after the transfer
                            print(f"Sender's account balance: ${self.account_balance} "
                                  f"\nReceiver's account balance: ${receiver_account.account_balance}\n")
                        else:
                            break       # if withdraw from the account is unsuccessful then the operation will break
                        break
                else:
                    # displays to tell the user that the account entered is not found hence transaction failed
                    print("Transaction failed!")
                    print("\nAccount referred to does not exist under Dangote bank."
                          "\nPlease verify the account number entered and try again\n")
            else:
                # displays a message to tell the user that they have insufficient money on their account and show balance
                print("\nTransaction failed!")
                print(f"There is no enough money on the account. \nAccount balance: ${self.account_balance}\n")

        except ValueError:  # displayed when the user's input type is invalid
            print('ONLY NUMBER ARE ALLOWED!!!!')
