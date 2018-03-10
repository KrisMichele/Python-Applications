import os

#------------------------------------------------------#
# Title: Module 5 - Assignment 05
# Dev:   Kristen Yang
# Date:  February 10, 2018
# ChangeLog: (revision number, Who, When, What)
#   initial revision, KY, 02/1018, Created starting template
#References:
# https://www.tutorialspoint.com/python/python_dictionary.htm
#https://www.pythoncentral.io/check-file-exists-in-directory-python/
#------------------------------------------------------#


#--- Data Definitions----------------------------------#
# file = An object that represents a file
# filePath = the path of file
# fileContents = An object used to read 'file'
# strData = A row of text data from the file
# dictionary = A dictionary data structure used to hold values and their associated keys
# intChoice = A menu of user options and variable to capture the user input


#--- Declare Variables and Constants-------------------#
filePath = "C:\\Users\\Kristen\\Dropbox\\Python Foundations\\Module05\\Homework\\Assigment05\\Todo.txt"
dictionary = dict()
list = []


#-- Input/Output ---------------------------------------#
# User can see list data (Step 4)
# User can see a Menu (Step 6)
# User can insert or delete data (Step 7 and 8)
# User can save to file (Step 9)
# Use can exit the program (Step 10)


#-- Processing Steps-------------------------------------#
# Step 1) Create a text file called Todo.txt.

# Step 2) When the program starts, load the any data you have
# in the text file called ToDo.txt into a python Dictionary.

#Step 3) Add dictionary contents to a list

#Step 4) Display the list contents to the user

#Step 5) Move into while loop and display a menu of choices to the user

#Step 6) Display all todo items to user

#Step 7) Add a new item to the list

#Step 8) Remove an item from the list

#Step 9) Save tasks to the ToDo.txt file

#Step 10) Exit program
#---------------------------------------------------------#


#-- Program-----------------------------------------------#
try:
    #Step 1) Create a text file called Todo.txt.
    if os.path.isfile(filePath):
        file = open(filePath, "r+")
        fileContents = file.read()
        if not fileContents:
            file.write("Task , Priority\nClean House , low\nPay Bills , high")
        file.close()
    else:
        file = open(filePath, "w")
        file.write("Task , Priority\nClean House , low\nPay Bills , high")
        file.close()


    # Step 2) When the program starts, load the any data you have
    # in the text file called ToDo.txt into a python Dictionary.
    file = open(filePath, "r")
    for line in file.readlines():
        strData = line
        key = (strData.split(",")[0]).strip()
        value = (strData.split(",")[1]).strip()
        dictionary[key] = value
    file.close()

except Exception as e: print("An error occurred:", e)



#Step 3) Add dictionary contents to a list
for key, value in dictionary.items():
    dictrow = {key : value}
    list.append(dictrow)


#Step 4) Display the list contents to the user
print("The tasks and priorities from Todo.txt are listed in the table below:")
for row in list:
    strData = (str(row)).strip("[{}]").replace("'", "")
    print("{}".format(strData))


#Step 5) Move into a while loop and display a menu of choices to the user
while (True):
    intChoice = int(input("\nEnter:\n'1' to show current data in the list\
    \n'2' to add a new item to the list,\
    \n'3' to remove an existing item from the list,\
    \n'4' to save data to the file,\
    \n'5' to exit the program:\n"))

    # Step 6) Display all todo items to user
    if intChoice == 1:
        for row in list:
            strData = (str(row)).strip("[{}]").replace("'", "")
            print("{}".format(strData))

    # Step 7) Add a new item to the list
    elif intChoice == 2:
        newTask = input("What is the new task?")
        newPriority = input("What is the priority for the new task?")
        newdictrow = {newTask : newPriority}
        list.append(newdictrow)
        print("You added {} to the list. ".format((str(newdictrow).strip("{}").replace("'",""))))

    # Step 8) Remove an item from the list
    elif intChoice == 3:
        removeItem = input("What is the item you would like to remove?")
        for row in list:
            if removeItem in row:
                list.remove(row)
                isFound = True
            else: isFound = False
        if isFound == True:
            print("Item '{}' and its priority were successfully deleted from the list.".format(removeItem))
        elif isFound == False:
            print("The item you entered could not be found in the list.")

    # Step 9) Save tasks to the ToDo.txt file
    elif intChoice == 4:
        try:
            file = open(filePath, "w")
            for row in list:
                strData = str(row).strip("[{}]").replace("'", "").replace(":",",")
                file.write(strData + "\n")
            file.close()
        except Exception as e: print("An error occurred:", e)


    # Step 10) Exit program
    elif intChoice == 5:
        print("You will now exit the menu")
        break;

    #Step 11) Default
    else:
        print("You did not enter a valid menu choice. Please enter a choice between 1 through 5.")