#----------------------------------------------------------#
# Title: CustomerChecking.py
# Dev:   Kristen Yang
# Date:  12Mar18
# Desc: This application manages customer name data
# ChangeLog: (Who, When, What) KY, 12Mar18, Initial Version
#----------------------------------------------------------#

if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")

class Customer(object):
    #Constructor
    def __init__(self, FirstName = "", LastName = "", TransactionID = 0):
        self.__FirstName = FirstName
        self.__LastName = LastName
        self.__TransactionID = TransactionID


    #Properties
    @property
    def FirstName(self):
        return self.__FirstName
    @FirstName.setter
    def FirstName(self, Value):
        self.__FirstName = Value

    @property
    def LastName(self):
        return self.__LastName
    @LastName.setter
    def LastName(self, Value):
        self.__LastName = Value

    @property
    def TransactionID(self):
        return self.__TransactionID
    @TransactionID.setter
    def TransactionID(self, Value):
        self.__TransactionID = Value


    #Methods
    def ToString(self):
        return str(self.TransactionID) + ", " + self.FirstName + " " + self.LastName


# ----------------end of class--------------------#