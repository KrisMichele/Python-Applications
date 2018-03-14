#----------------------------------------------------------#
# Title: CustomerChecking.py
# Dev:   Kristen Yang
# Date:  12Mar18
# Desc: This is the Main Program for the Application
# ChangeLog: (Who, When, What) KY, 12Mar18, Initial Version
#----------------------------------------------------------#

if __name__ == "__main__":
    import CustomerWithdrawl, CustomerDeposit, SaveCustomerData, Customers
else:
    raise Exception("This file was not created to be imported")

#----------------Data--------------------------------------#
# declare variables and constants\
WObj = None #the withdrawl object
DObj = None #the deposit object
strFirstName = "" #The customer First Name
strLastName = "" #The customer Last Name
fltWithdrawlAmount = 0.00 #Inital Withdrawl Amount
fltDepositAmount = 0.00 #Initial Deposit Amount
fltTotalBalance = 1000.00 #Current Balance
intTransactionID = 0 #Initial TransactionID per Customer

#--------------Factory Functions---------------------------#
def ProcessWithdrawls(TransactionID, FirstName, LastName, WithdrawlAmount, TotalBalance):
    try:
        WObj = CustomerWithdrawl.Withdrawl()
        WObj.TransactionID = TransactionID
        WObj.FirstName = FirstName
        WObj.LastName = LastName
        WObj.WithdrawlAmount = WithdrawlAmount
        WObj.TotalBalance = TotalBalance
        WObj.CurrentTime = CustomerWithdrawl.Withdrawl.TransactionTime(WObj)
        RemainingBalance = CustomerWithdrawl.Withdrawl.BalanceCalc(WObj)
        CustomerWithdrawl.WithdrawlsList.AddWithdrawl(WObj)
        return RemainingBalance
    except Exception as e:
        print(e)

def ProcessDeposits(TransactionID, FirstName, LastName, DepositAmount, TotalBalance):
    try:
        DObj = CustomerDeposit.Deposit()
        DObj.TransactionID = TransactionID
        DObj.FirstName = FirstName
        DObj.LastName = LastName
        DObj.DepositAmount = DepositAmount
        DObj.TotalBalance = TotalBalance
        DObj.CurrentTime = CustomerDeposit.Deposit.TransactionTime(DObj)
        RemainingBalance = CustomerDeposit.Deposit.BalanceCalc(DObj)
        CustomerDeposit.DepositList.AddDeposit(DObj)
        return RemainingBalance
    except Exception as e:
        print(e)

def SaveDataToFile(choice):
    try:
        SaveObj = SaveCustomerData.File()
        SaveObj.FileName = "C:\_PythonClass\Module 9\CustomerTransactions.txt"
        if choice == "w": SaveObj.Data = CustomerWithdrawl.WithdrawlsList.ToString()
        elif choice == "d": SaveObj.Data = CustomerDeposit.DepositList.ToString()
        SaveObj.SaveData()
    except Exception as e: print(e)



#----Presentation IO Functions-----------------------------#
#Menu Function
def MenuInput():
    menu = input("Enter one of the following options for the customer: "
                    "\n'w' to process withdrawls from the customer's bank account"
                    "\n'd' to process deposits to the customer's bank account."
                    "\n'q' to quit the menu")
    return menu

def CustomerNameInput():
    firstname = input("Enter the First Name of the Customer:")
    lastname = input("Enter the Last Name of the Customer:")
    return firstname, lastname

def WithdrawAmountInput():
    amount = float(input("Enter in the withdrawl amount (Current bank account balance is: " + str(fltTotalBalance) + "):"))
    return amount

def DepositAmountInput():
    amount = float(input("Enter in the deposit amount (Current bank account balance is " + str(fltTotalBalance) + "):"))
    return amount

def DisplayWithdrawlBalance():
    print("The Transaction Data is: ")
    print("------------------------")
    print(CustomerWithdrawl.WithdrawlsList.ToString())

def DisplayDepositBalance():
    print("The Transaction Data is: ")
    print("------------------------")
    print(CustomerDeposit.DepositList.ToString())

def OverdraftingMsg():
    print("The customer does not have enough funds in their bank account to process the request.")

def DefaultMsg():
    print("You did not enter a valid option. Please retry.")


#------------------Main Program-----------------------------#
strFirstName, strLastName = CustomerNameInput()

while(True):
    strMenu = MenuInput()
    if strMenu.lower() == "w":
        fltWithdrawlAmount = WithdrawAmountInput()
        if fltTotalBalance > fltWithdrawlAmount:
            fltRemainingBalance = ProcessWithdrawls(intTransactionID, strFirstName, strLastName, fltWithdrawlAmount, fltTotalBalance)
            fltTotalBalance = fltRemainingBalance
            intTransactionID += 1
            DisplayWithdrawlBalance()
            SaveDataToFile(strMenu)
        else:
            OverdraftingMsg()

    elif strMenu.lower() == "d":
        fltDepositAmount = DepositAmountInput()
        fltRemainingBalance = ProcessDeposits(intTransactionID, strFirstName, strLastName, fltDepositAmount, fltTotalBalance)
        fltTotalBalance = fltRemainingBalance
        intTransactionID += 1
        DisplayDepositBalance()
        SaveDataToFile(strMenu)

    elif strMenu.lower() == "q": break

    else: DefaultMsg()

