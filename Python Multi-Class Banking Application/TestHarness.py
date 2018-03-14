#----------------------------------------------------------#
# Title: CustomerChecking.py
# Dev:   Kristen Yang
# Date:  12Mar18
# Desc: This is the Test Harness for the Application
# ChangeLog: (Who, When, What) KY, 12Mar18, Initial Version
#----------------------------------------------------------#


if __name__ == "__main__":
    import Customers, CustomerWithdrawl, CustomerDeposit, SaveCustomerData
else:
    raise Exception("This file was not created to be imported")

print("\n-----------------------------------")
print("Test the Customers.Customer class:")
CustomerObj = Customers.Customer()
CustomerObj.FirstName = "TestFirstName"
CustomerObj.LastName = "TestLastName"
CustomerObj.TransactionID = 1
print(CustomerObj.ToString())

print("\n-----------------------------------")
print("Test the CustomerWithdrawl.Withdrawl class:")
CWObj = CustomerWithdrawl.Withdrawl()
CWObj.TransactionID = 2
CWObj.FirstName = "Sue"
CWObj.LastName = "Jones"
CWObj.WithdrawlAmount = 10.00
CWObj.TotalBalance = 1000.00
RemainingBalance = CWObj.BalanceCalc()
print(RemainingBalance)
CWObj.CurrentTime = CWObj.TransactionTime()
print(CWObj.ToString())

print("\n-----------------------------------")
print("Test the CustomerWithdrawl.WithdrawlList class:")
CWListObj = CustomerWithdrawl.WithdrawlsList()
try:
    print("Trying the wrong object type:")
    CWListObj.AddWithdrawl(CustomerObj)
    CWListObj.ToString()
except:
    print("The object CustomerObj is not a Withdrawl object. This should fail.")
try:
    print("Trying the right object type:")
    CWListObj.AddWithdrawl(CWObj)
    print(CWListObj.ToString())
except:
    print("The object CWObj is a Withdrawl object. This shoud not fail.")


print("\n-----------------------------------")
print("Test the CustomerDeposit.Deposit class:")
CDObj = CustomerDeposit.Deposit()
CDObj.TransactionID = 3
CDObj.FirstName = "Bob"
CDObj.LastName = "Smith"
CDObj.DepositAmount = 50.00
CDObj.TotalBalance = 2000.00
RemainingBalance = CDObj.BalanceCalc()
print(RemainingBalance)
CDObj.CurrentTime = CDObj.TransactionTime()
print(CDObj.ToString())


print("\n-----------------------------------")
print("Test the CustomerDeposit.DepositList class:")
CDListObj = CustomerDeposit.DepositList()
try:
    print("Trying the wrong object type:")
    CDListObj.AddDeposit(CustomerObj)
    CDListObj.ToString()
except:
    print("The object CustomerObj is not a Deposit object. This should fail.")
try:
    print("Trying the right object type:")
    CDListObj.AddDeposit(CDObj)
    print(CDListObj.ToString())
except:
    print("The object CDObj is a Deposit object. This shoud not fail.")


print("\n-----------------------------------")
print("Test the SaveCustomerData.File class:")
CSaveDataObj = SaveCustomerData.File()
CSaveDataObj.FileName = "Test.txt"
CSaveDataObj.Data = "\nThis is Test Data"
CSaveDataObj.SaveData()
print("The data retrieved from Test.txt is: " + CSaveDataObj.GetData())


