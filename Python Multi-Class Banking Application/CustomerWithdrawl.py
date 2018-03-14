#----------------------------------------------------------#
# Title: CustomerChecking.py
# Dev:   Kristen Yang
# Date:  12Mar18
# Desc: This application manages customer withdrawls
# ChangeLog: (Who, When, What) KY, 12Mar18, Initial Version
#----------------------------------------------------------#

import Customers, datetime

if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")


class Withdrawl(Customers.Customer):

    #--Constructor--
    def __init__(self, WithdrawlAmount = 0.00, TotalBalance = 0.00):
        self.__WithdrawlAmount = WithdrawlAmount
        self.__TotalBalance = TotalBalance

    #--Properties--
    @property
    def WithdrawlAmount(self):
        return self.__WithdrawlAmount
    @WithdrawlAmount.setter
    def WithdrawlAmount(self, Value):
        self.__WithdrawlAmount = Value

    @property
    def TotalBalance(self):
        return self.__TotalBalance
    @TotalBalance.setter
    def TotalBalance(self, Value):
        self.__TotalBalance = Value


    #--Methods--
    def BalanceCalc(self):
        return self.TotalBalance - self.WithdrawlAmount

    def TransactionTime(self):
        CurrentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        return CurrentTime

    def ToString(self):
        return "Date/Time:" + str(self.CurrentTime) + ",  Name:" + self.FirstName + " " + self.LastName + ",  Transaction ID: " + str(self.TransactionID) +  ",  Withdrawl Amount:" + str(
                self.WithdrawlAmount) + ",  Remaining Balance:" + str(self.TotalBalance - self.WithdrawlAmount) + "\n"
# ----------------end of class--------------------#


class WithdrawlsList(object):
    #--Fields--
    __CustWithdrawls = []  #The list of all the withdrawls from the customer's bank account

    #--Methods--
    @staticmethod
    def AddWithdrawl(Withdrawl):
        if (str(Withdrawl.__class__) == "<class 'CustomerWithdrawl.Withdrawl'>"):
            WithdrawlsList.__CustWithdrawls.append(Withdrawl)
        else:
            raise Exception("Only Withdrawl transactions can be added to this list")

    @staticmethod
    def ToString():
        strData = ""
        for item in WithdrawlsList.__CustWithdrawls:
            strData = "Date/Time:" + str(item.CurrentTime) + ",  Name:" + item.FirstName + " " + item.LastName + ",  Transaction ID: " + str(item.TransactionID) +  ",  Withdrawl Amount:" + str(
                item.WithdrawlAmount) + ",  Remaining Balance:" + str(item.TotalBalance - item.WithdrawlAmount) + "\n"
        return strData

# ----------------end of class--------------------#