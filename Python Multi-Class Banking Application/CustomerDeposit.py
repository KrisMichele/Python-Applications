#----------------------------------------------------------#
# Title: CustomerChecking.py
# Dev:   Kristen Yang
# Date:  12Mar18
# Desc: This application manages customer deposits
# ChangeLog: (Who, When, What) KY, 12Mar18, Initial Version
#----------------------------------------------------------#

import Customers, datetime

if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")

class Deposit(Customers.Customer):
    #Constructor
    def __init__(self, DepositAmount = 0.00, TotalBalance = 0.00):
        self.__DepositAmount = DepositAmount
        self.__TotalBalance = TotalBalance

    #Properties
    @property
    def DepositAmount(self):
        return self.__DepositAmount
    @DepositAmount.setter
    def DepositAmount(self, Value):
        self.__DepositAmount = Value

    @property
    def TotalBalance(self):
        return self.__TotalBalance
    @TotalBalance.setter
    def TotalBalance(self, Value):
        self.__TotalBalance = Value

    #---Methods---------
    def BalanceCalc(self):
        return self.TotalBalance + self.DepositAmount

    def TransactionTime(self):
        CurrentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        return CurrentTime

    def ToString(self):
        return "Date/Time:" + str(self.CurrentTime) + ",  Name:" + self.FirstName + " " + self.LastName + ",  Transaction ID: " + str(self.TransactionID) +  ",  Deposit Amount:" + str(
                self.DepositAmount) + ",  Remaining Balance:" + str(self.TotalBalance + self.DepositAmount) + "\n"

# ----------------end of class--------------------#


class DepositList(object):
    #--Fields--
    __CustDeposits = []  #The list of all the deposits into the customer's bank account

    #--Methods--
    @staticmethod
    def AddDeposit(Deposit):
        if (str(Deposit.__class__) == "<class 'CustomerDeposit.Deposit'>"):
            DepositList.__CustDeposits.append(Deposit)
        else:
            raise Exception("Only Deposit transactions can be added to this list")

    @staticmethod
    def ToString():
        strData = ""
        for item in DepositList.__CustDeposits:
            strData = "Date/Time:" + str(item.CurrentTime) + ",  Name:" + item.FirstName + " " + item.LastName + ",  Transaction ID: " + str(item.TransactionID)+ ",  Deposit Amount:" + str(
                item.DepositAmount) + ",  Remaining Balance:" + str(item.TotalBalance + item.DepositAmount) + "\n"
        return strData

# ----------------end of class--------------------#