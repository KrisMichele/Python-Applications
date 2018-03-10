#-----------------------------------------------------------------------------#
# Title: Module 7 - Assignment 07
# Dev:   Kristen Yang
# Date:  February 26, 2018
# Change Log: (revision number, Who, When, What)
#   Rev. 0 (Assignment 07), KY, 02/26/18, Create Script Using Pickle Module
# References:
#1) Michael Dawson. Python Programming for the Absolute Beginner.
#   Third Edition, Chapter 7. Boston, MA: Course Technology, 2010.

#2) Randall Root. "Module 07 Programming Notes." (2018): all pages.
#    https://canvas.uw.edu/courses/1177874/files/44880387?module_item_id=7923725>

#3) Python Software Foundation, “Python 3.3.7 Documentation –
#   Python Object Serialization” (2017).
#   <https://docs.python.org/3.3/library/pickle.html?highlight=pickle#module-pickle>

#4) Youtube Tutorial by sentdex, “Python Pickle Module for
#   Saving Objects (Serialization)” (2015).
#   <https://www.youtube.com/watch?v=2Tw39kZIbhs
#----------------------------------------------------------------------------#

#Import Required Modules-----------------------------------------------------#
import pickle
import random


#--- Declare Variables and Constants-----------------------------------------#
FileName = "C:\\_PythonClass\\Module 7\\EmployeeOnboarding.pickle"
strUserInput = ""
EmpName = ""
EmpPassword = ""
LetterString = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
NumString = "1234567890"
DefaultPswLength = 8
PasswordList = []
ListStruct = []


#-- Data Processing Class and Functions---------------------------------------#
class ProcessInfo(object):
    @staticmethod
    def CheckFileContents(filePath):
        '''
        This function is used to check if a binary file is created at the
        correct file path. If it is not created, then the file will be during
        execution of the exception handling block.
        :param file - The file at path filePath opened in read binary format.
        :param filePath - The filepath for EmployeeOnboarding.pickle.
        :param fileList - The list of data containing the employee name and associated password.
        '''
        fileList = [["Name", "Password"]]
        try:
            file = open(filePath, 'rb+')
            pickle.load(file)
            file.close()
        except Exception as e:
            print("An error occurred:", e)
            file = open(filePath, 'wb')
            pickle.dump(fileList, file)
            file.close()

    @staticmethod
    def ReadFile(filePath):
        '''
        This function is used to load any contents from EmployeeOnboarding.pickle to a list.
        :param file - The file at path filePath opened in read binary format.
        :param filePath - The filepath for EmployeeOnboarding.pickle.
        :param fileList - The list of data containing the employee name and associated password.
        '''
        file = open(filePath, "rb")
        fileList = pickle.load(file)
        file.close()
        return fileList

    @staticmethod
    def RandPswGen(letterData, numberData,pswLength,pswList):
        '''
        This function generates a random 8 character password, with odd indexes being
        letter characters and even indexes being number characters.
        :param letterData - A string of upper and lowercase letter characters.
        :param numberData - A string of numerical characters.
        :param pswLength - The length required for the password.
        :param pswList - A list used to store characters during execution of the while loop.
        :return: The password list data returned as a string.
        '''
        while len(pswList) < pswLength:
            if len(pswList) % 2 == 0:
                #if the index is even, choose an uppercase or lowercase letter
                pswList.append(random.choice(letterData))
            else:
                #if the index is odd, choose a number
                pswList.append(random.choice(numberData))
        return ''.join(pswList)


    @staticmethod
    def AppendList(name, password, fileList):
        '''
        This function is used to load the employee username and random password
        into a list that can be written to a binary file.
        :param name - The employee name variable.
        :param password - The random password variable.
        :param fileList - A list to hold the name and password.
        '''
        data = [name, password]
        fileList.append(data)




    @staticmethod
    def WriteFile(fileList, filePath):
        '''
        This function is used to write contents from the list to EmployeeOnboarding.pickle.
        :param file - The file at path filePath opened in read binary format.
        :param filePath - The filepath for EmployeeOnboarding.pickle.
        :param fileList - The list of data containing the employee name and associated password.
        '''
        file = open(filePath, "wb")
        pickle.dump(fileList, file)
        file.close()


#-- Input / Output Class and Functions----------------------------------------#
class IO(object):
    @staticmethod
    def DisplayList(fileList):
        '''
        This function is used to display the contents of the list.
        :param filePath - The filepath for EmployeeOnboarding.pickle.
        '''
        print("The file contents are:")
        print(fileList)


    @staticmethod
    def UserMenu():
        '''
        This function is used to display the menu choices to the user and capture user input.
        :return strInput - The menu choice specified by the user.
        '''
        strInput = input("Enter 'y' to enter a New Employee with Random Password into the Employee Onboarding pickle file, \
        \nor press any other key to exit.")
        return strInput

    @staticmethod
    def UserName():
        '''
        This function is used to capture the employee name entered by the user.
        :return name - The name entered by the user.
        '''
        name = input("What is the new Employee First and Last Name: ")
        return name




#-- Main Method---------------------------------------------------------------#
#Step 1) Create Objects for each Class
objectIO = IO()
objectPrInfo = ProcessInfo()

#Step 2) Check if File is Created and Create, if Required
objectPrInfo.CheckFileContents(FileName)

#Step 3) Load the Contents from the File into a List and Display
ListStruct = objectPrInfo.ReadFile(FileName)
objectIO.DisplayList(ListStruct)

#Step 4) Create Menu to Enter Name and Generate Password
while(True):
    strUserInput = objectIO.UserMenu()
    if strUserInput.lower() == "y":
        EmpName = objectIO.UserName()
        EmpPassword = objectPrInfo.RandPswGen(LetterString,NumString,DefaultPswLength,PasswordList)
        objectPrInfo.AppendList(EmpName, EmpPassword, ListStruct)
    else: break

#Step 5) Write List Contents to File
objectPrInfo.WriteFile(ListStruct, FileName)
