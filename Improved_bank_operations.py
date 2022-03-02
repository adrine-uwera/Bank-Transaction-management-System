# file for the improved main function
import W7_A3_Q3_Adrine_Uwera_current_account  # imports current account file  as whole because all codes in the file are needed
import W7_A3_Q2_Adrine_Uwera_savings_account  # imports savings account file  as whole because all codes in the file are needed
import W7_A3_Q1_Adrine_Uwera_class_account  # imports class account file  as whole because all codes in the file are needed


# function that controls the flow of operations according to user's choice
# this function will allow the user to create an account, view account balance, deposit money into an account,
# withdraw money from the account transfer money between accounts, claim interest returns on money in the bank,
# view account details for an account and display all account details record of dangote
def main():
    print("\nDangote bank")
    print("------------")
    start = 'Y'  # the variable is initiated at Y yo represent yes so as to automatically allow the user to do the first operation

    while True:  # loop through the operations and allow the user to do operations without having to restart the program over and over again
        try:
            if start.upper() == 'Y':  # checks if the user wants to do a business operation
                print("\nList of bank operations:"
                      "\n 1: Create an account, \n 2: View account balance,"
                      "\n 3: Deposit money into an account, \n 4: Withdraw money"
                      "\n 5: Transfer money, \n 6: Claim interest returns "
                      "\n 7: View account details"
                      "\n 8: View all account records "
                      "\n or any key to exit.")  # display the list of operations the user can do
                operation = input("\nEnter number respectively matching the operation to be performed: ")  # asks user to choose operation to do

                if operation == '1':  # if user chooses to create account
                    print("\nCreate account")
                    print("--------------")
                    account_type = input("Types of account: \n 1: Current account\n 2: Savings account"
                                         "\n Enter number respectively matching the type of account used: ")  # asks the user the to choose the type of account to be created
                    if account_type == '1':  # if user wants to create a current account
                        print("\nPersonal details:")
                        account_details = W7_A3_Q3_Adrine_Uwera_current_account.CurrentAccount(
                            name=input("Enter account holder's full name: "),
                            age=input("Enter account holder's age in figures: "),
                            gender=input("Enter account holder's gender (F/M): "),
                            occupation=input("Enter account holder's occupation(if any): "))  # creates an instance of current account class and allow the user to pass in account details
                        print("\nCurrent account was created successfully!")  # message to indicate that the account was created
                        print(account_details)  # displays account details after the account is successfully created
                    elif account_type == "2":  # if user wants to create a savings account
                        print("\nPersonal details:")
                        account_details = W7_A3_Q2_Adrine_Uwera_savings_account.SavingsAccount(
                            name=input("Enter account holder's full name: "),
                            age=input("Enter account holder's age in figures: "),
                            gender=input("Enter account holder's gender (F/M): "),
                            occupation=input("Enter account holder's occupation(if any): "))  # creates an instance of savings account class and allow the user to pass in account details
                        print("\nSaving account was created successfully!")  # message to indicate that the account was created
                        print(account_details)  # displays account details after the account is successfully created

                    else:
                        # displays when the user enter another number or any other input other than 1 or 2
                        print("\nInvalid input. \nChoose between the specified options.\n")

                elif operation == '2':  # if user chooses to view account balance account
                    print("\nView balance")
                    print("------------")
                    acc_nbr1 = int(input("Enter account number of the account to view balance: "))  # asks the user the account to view balance for
                    for account in W7_A3_Q1_Adrine_Uwera_class_account.dangote_account_records:   # loops through the list of account details
                        if acc_nbr1 == account.account_number:  # checks if the the account is under dangote bank
                            account.view_account_balance()  # displays the account balance of the specified account
                            break
                    else:
                        # displays to tell the user that the account referred to is not found hence transaction failed
                        print("\nAccount referred to does not exist under Dangote bank. "
                              "\nPlease verify the account number entered and try again\n")

                elif operation == '3':  # if user chooses to deposit money in a bank account
                    print("\nDeposit money")
                    print("-------------")
                    acc_nbr2 = int(input("Enter account number of the account in which to deposit money: "))    # asks the user the account to deposit money in
                    for account in W7_A3_Q1_Adrine_Uwera_class_account.dangote_account_records:   # loops through the list of account details
                        if acc_nbr2 == account.account_number:   # checks if the the account is under dangote bank
                            money_deposited = float(input("Enter the amount of money to deposit in numerical form: $"))  # asks the user the amount of money to be deposited
                            account.deposit_money(money_deposited)  # calls the method for depositing money and pass in the money to be deposited
                            break
                    else:
                        # displays to tell the user that the account referred is not found hence transaction failed
                        print("\nTransaction failed!")
                        print("\nAccount referred to does not exist under Dangote bank."
                              "\nPlease verify the account number entered and try again\n")

                elif operation == '4':  # if user chooses to withdraw money from a bank account
                    print("\nWithdraw money")
                    print("-------------")
                    acc_nbr3 = int(input("Enter account number of the account from which to withdraw money: ")) # asks the user the account from which the money will be withdrawn
                    for account in W7_A3_Q1_Adrine_Uwera_class_account.dangote_account_records:    # loops through the list of account details
                        if acc_nbr3 == account.account_number:  # checks if the the account is under dangote bank
                            money_withdrawn = float(input("Enter the amount of money to withdraw in numerical form: $"))   # asks the user the amount of money to be withdrawn
                            account.withdraw_money(money_withdrawn) # calls the method for withdrawing money and pass in the money to be withdrawn
                            break
                    else:
                        # displays to tell the user that the account referred is not found hence transaction failed
                        print("\nTransaction failed!")
                        print("\nAccount referred to does not exist under Dangote bank."
                              "\nPlease verify the account number entered and try again\n")

                elif operation == '5':  # if user chooses to transfer money to another a bank account
                    print("\nTransfer money")
                    print("--------------")
                    acc_nbr4 = int(input("Enter account number of the sender account: "))   # asks the user the account from which the money will be transfered from (sender's acoount)
                    for sender_account in W7_A3_Q1_Adrine_Uwera_class_account.dangote_account_records:     # loops through the list of account details
                        if acc_nbr4 == sender_account.account_number:   # checks if the the account is under dangote bank
                            sender_account.transfer_money()  # calls the method for transferring money
                            break
                    else:
                        # displays to tell the user that the account referred is not found hence transaction failed
                        print("\nTransaction failed!")
                        print("\nAccount referred to does not exist under Dangote bank."
                              "\nPlease verify the account number entered and try again\n")

                elif operation == "6":  # if user chooses to claim interest returns on the money that's been in the bank
                    print("\nClaim interest returns")
                    print("----------------------")
                    acc_nbr7 = int(input("Enter account number of the account for which to claim returns: "))
                    for account in W7_A3_Q1_Adrine_Uwera_class_account.dangote_account_records:    # loops through the list of account details
                        if acc_nbr7 == account.account_number:  # checks if the the account is under dangote bank
                            account.add_interest()  # calls the method for adding interest to the account
                            break
                    else:
                        # displays to tell the user that the account referred is not found hence transaction failed
                        print("\nAccount referred to does not exist under Dangote bank."
                              "\nPlease verify the account number entered and try again\n")

                elif operation == "7":  # if user chooses to view details of an account
                    acc_nbr6 = int(input("Enter account number of the account for which to view details: "))
                    for account in W7_A3_Q1_Adrine_Uwera_class_account.dangote_account_records:    # loops through the list of account details
                        if acc_nbr6 == account.account_number:  # checks if the the account is under dangote bank
                            print(account)  # displays the account details for the account specified
                            break
                    else:
                        # displays to tell the user that the account referred is not found
                        print("\nAccount referred to does not exist under Dangote bank."
                              "\nPlease verify the account number entered and try again\n")

                elif operation == "8":   # if user chooses to view details of all accounts in dangote bank
                    print("\nDangote Accounts records")
                    print("------------------------")
                    for account in W7_A3_Q1_Adrine_Uwera_class_account.dangote_account_records:    # loops through the list of account details
                        print(f"Account number:{account.account_number} "
                              f"\nAccount holder's name: {account.name}"
                              f" \n"f"Account balance: ${account.account_balance} \n")  # displays the main account details for all the accounts in dangote

                else:
                    # exits the program in case the user enters other key
                    print("\nYou exited the program!\n")
                    break

                # asks the user if he/she wants to do another operation
                start = input("Enter 'Y' to do another bank operation or any other key to exit: ")
            else:
                # exits the program in case the user enters other key
                print("\nYou exited the program!\n")
                break
        except ValueError:  # displayed when the user's input type is invalid
            print('ONLY NUMBER ARE ALLOWED!!!!')


# This code calls the 'main' function
if __name__ == '__main__':
    main()
