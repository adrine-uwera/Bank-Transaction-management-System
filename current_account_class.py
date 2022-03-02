# File for Current Account (child class)

import W7_A3_Q1_Adrine_Uwera_class_account    # imports class account file as whole because all codes in the file are needed
import math             # imports math library
from _datetime import datetime      # imports the datetime class from datetime module in python


# class for current account
class CurrentAccount(W7_A3_Q1_Adrine_Uwera_class_account.Account):    # a class named CurrentAccount which inherited Client class
    # inherited Account class from class_account file because current account is an account but with more functionality

    interest_rate = 0.01  # variable for the interest earn by a client when his/her money stays in the bank for a month
    # 0.01 is equivalent to 1%

    # a method that calculate and add interest to the client's account after the respective period
    def add_interest(self):

        # variable that takes in user input to specify the period the money has been in the bank
        period = float(input("For how many months has the money been in the bank since the last interest deposit? "
                             "\nor when was the last time you withdrew money from the account?"
                             "\nEnter the number of months in figures: "))

        # a variable for 1 month period that the money must stay in the bank in order to earn an interest
        interest_period = 1

        # round the number down to the nearest integer in case the user enters an decimal number
        # decimal number means that the month would have been in the bank for n months and some days
        # the number is round down to the nearest integer because the decimals after the whole number of month
        # are not a complete month so the client won't get interest for incomplete month.
        period = math.floor(period)

        if period >= interest_period:  # checks the period the money has been in the bank is greater than 1 month
            # calculates the interest with respect to the amount of time the money has been in the bank for
            self.account_balance = self.account_balance * (1 + self.interest_rate) ** period
            date_interest_dep = datetime.now()         # records the date when the money was withdrawn
            print(f"Date of interest deposit: {date_interest_dep}")  # displays the date when the interest was deposited
            self.view_account_balance()  # displays the account balance after adding interest
        else:
            # displays a message to tell the user that the 1 month period is not yet over
            print("Insufficient period. You can only receive interest after at least a period of one month.")
