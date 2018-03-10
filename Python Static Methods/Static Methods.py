import os

#-----------------------------------------------------------------------------#
# Title: Module 6 - Assignment 06
# Dev:   Kristen Yang
# Date:  February 19, 2018
# Change Log: (revision number, Who, When, What)
#   Rev. 0 (Assignment 05), KY, 02/11/18, Created starting template
#   Rev. 1 (Assignment 06), KY, 02/19/18, Revise to implement classes &
#   functions
# References:
# https://canvas.uw.edu/courses/1177874/assignments/3947573?module_item_id=7923721
# https://www.pythoncentral.io/check-file-exists-in-directory-python/
#----------------------------------------------------------------------------#



#--- Declare Variables and Constants------------------------------------------#
"""
fileName is the filepath for Todo.txt.
dictStruct is the dictionary data structure used to hold tasks and their associated priorities.
listStruct is the list data structure used to hold dictionary rows to create a tabular format.
"""
fileName = "C:\\Users\\Kristen\\Dropbox\\Python Foundations\\Module06\\Homework\\Assignment06\\Todo.txt"
dictStruct = dict()
listStruct = []



#-- Data Processing Class and Functions---------------------------------------#
class ProcessFile(object):

    @staticmethod
    def CreateFile(filePath):
        """
        Creates a file called Todo.txt at filePath if the file doesn't exist.
        Writes two tasks and priorities to the file if the file contents
        are empty.
        :param file - The file at path filePath opened in read or write format
        :param filePath - The path of the text file Todo.txt
        :param fileContents - A variable to hold the file contents as Todo.txt is read.
        """
        try:
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
        except Exception as e: print("An error occurred:", e)



    @staticmethod
    def LoadData(filePath, dictionary):
        """
        Reads the data from Todo.txt and loads it into a Python dictionary.
        :param filePath - The path of the text file Todo.txt.
        :param file - The file at path filePath opened in read format
        :param strData - A variable to contain each line of data in filePath as the file is read.
        :param key - The key of a particular dictionary row which is the task.
        :param value - The value of a particular dictionary row, which is the priority of the task.
        :param dictionary - The dictionary data structure used to hold tasks and their priorities.
        """
        try:
            file = open(filePath, "r")
            for line in file.readlines():
                strData = line
                key = (strData.split(",")[0]).strip()
                value = (strData.split(",")[1]).strip()
                dictionary[key] = value
            file.close()
        except Exception as e: print("An error occurred:", e)



    @staticmethod
    def MoveToList(dictionary, list):
        """
        Add dictionary contents to a list.
        :param dictionary - The dictionary data structure used to hold tasks and their priorities.
        :param dictRow - A particular dictionary row that will be added to the list.
        :return list - The list data structure used to hold the dictionary keys and values in a tabular format.
        """
        for key, value in dictionary.items():
            dictRow = {key : value}
            list.append(dictRow)
        return list


    @staticmethod
    def AddTask(list, addTask, addPriority):
        """
        Add task and priority to list.
        :param addTask - The new task (dictionary key) that will be added.
        :param addPriority - The priority (dictionary value) for newTask that will be added.
        :param newDictRow -  A new dictionary row holding newTask and newPriority that will be added to the list.
        :param list - The list data structure used to hold the dictionary keys and values in a tabular format.
        :param lastRow - The last row in the list.
        :return isAdded - A boolean variable used to indicate whether the new task was added or not to the list.
        """
        newDictRow = {addTask: addPriority}
        list.append(newDictRow)
        lastRow = list[-1];
        if newDictRow == lastRow:
            isAdded = True
        else: isAdded = False
        return isAdded


    @staticmethod
    def DeleteTask(list, deleteTask):
        """
        Remove a task and priority from the list.
        :param list - The list data structure used to hold the dictionary keys and values in a tabular format.
        :param deleteTask - The dictionary key representing the task that will be removed from the list.
        :return isFound - A boolean variable used to indicate whether deleteTask is found in the list or not
        """
        for row in list:
            if deleteTask in row:
                list.remove(row)
                isFound = True
            else:
                isFound = False
        return isFound


    @staticmethod
    def SaveFile(filePath, list):
        """
        Saves the list with its dictionary contents to Todo.txt.
        :param file - The file at path filePath opened in write format.
        :param filePath - The path of the text file Todo.txt.
        :param list - The list data structure used to hold the dictionary keys and values in a tabular format.
        :param strData - A single row in list converted to the string format that will be written to the text file.
        :return isSaved - A boolean variable used to indicate whether the file was successfully saved or not.
        """
        try:
            file = open(filePath, "w")
            for row in list:
                strData = str(row).strip("[{}]").replace("'", "").replace(":",",")
                file.write(strData + "\n")
            file.close()
            isSaved = True
        except Exception as e:
            print("An error occurred:", e)
            isSaved = False
        return isSaved





#-- Input Class and Functions-------------------------------------------------#
class Inputs(object):

    @staticmethod
    def DisplayChoices():
        """
        Displays a menu of choices to the user.
        :return choices - A menu of user options used to capture the user input
        """
        choices = input("\nEnter:\n'1' to show current data in the list\
        \n'2' to add a new task and priority to the list,\
        \n'3' to remove an existing task and priority from the list,\
        \n'4' to save data to the file,\
        \n'5' to exit the program:\n")
        return choices


    @staticmethod
    def InputNewTask():
        """
        Enter in a new task into the dictionary within the list
        :return addTask - The new task that will be added to the list
        :return addPriority - The new priority that will be added to the list
        """
        addTask = input("What is the new task?")
        addPriority = input("What is the priority for the new task?")
        return addTask, addPriority


    @staticmethod
    def InputTaskToDelete():
        """
        Enter in a task you wish to delete from the list
        :return deleteTask - The task that will be removed.
        """
        deleteTask = input("What is the task you would like to remove?")
        return deleteTask



#-- Output Class and Functions------------------------------------------------#
class Outputs(object):

    @staticmethod
    def DisplayList(list):
        """
        Display the contents of the list.
        :param list - The list data structure used to hold the dictionary keys and values in a tabular format.
        :param strData - A single row in list converted to the string format that will be displayed to the user
        """
        print("The tasks and priorities from the list are listed in the table below:")
        for row in list:
            strData = (str(row)).strip("[{}]").replace("'", "")
            print("{}".format(strData))


    @staticmethod
    def AddTaskStatus(isAdded, addedTask, addedPriority):
        """
        Displays the task and priority that was added to the list.
        :param addedTask - The new task that was added as a dictionary key to the list.
        :param addedPriority - The new priority that was added as a dictionary value to the list.
        :param isAdded - A boolean variable used to indicate whether the new task was added or not to the list.
        """
        if isAdded == True:
            print("You successfully added {} to the list. ".format("Task: '" + addedTask + "' and Priority: '" + addedPriority + "'"))
        elif isAdded == False:
            print("You did not successfully add '{}' to the list. ".format("Task: '" + addedTask + "' and Priority: '" + addedPriority + "'"))


    @staticmethod
    def DeleteTaskStatus(isFound, deletedTask):
        """
        Displays the task that was deleted from the list, if applicable.
        :param isFound - A boolean variable used to indicate whether deletedTask is found in the list or not.
        :param deletedTask - The task that was removed.
        """
        if isFound == True:
            print("Task '{}' and its priority were successfully deleted from the list.".format(deletedTask))
        elif isFound == False:
            print("Task '{}' could not be found in the list.".format(deletedTask))

    @staticmethod
    def FileSavedStatus(isSaved):
        """
        :param isSaved - A boolean variable used to indicate whether the file was successfully saved or not.
        """
        if isSaved == True:
            print("The contents in the list were successfully saved to Todo.txt.")
        if isSaved == False:
            print("The file Todo.txt could not be saved.")


    @staticmethod
    def ExitMenu():
        """
        Displays that the user is exiting the menu.
        """
        print("You will now exit the menu")

    @staticmethod
    def Default():
        """
        Displays that the user entered an incorrect choice for strChoices
        """
        print("You did not enter a valid menu choice. Please enter a choice between 1 through 5.")


#-- Main Method---------------------------------------------------------------#

#Step 1) Create a text file called Todo.txt:
FileCreation = ProcessFile.CreateFile(fileName)


# Step 2) When the program starts, load the any data you have
# in the text file called ToDo.txt into a python Dictionary:
LoadData = ProcessFile.LoadData(fileName, dictStruct)


# Step 3) Add dictionary contents to a list:
AddDictToList = ProcessFile.MoveToList(dictStruct, listStruct)



#Step 4) Move into a while loop and display a menu of choices to the user
while (True):
    strChoices = Inputs.DisplayChoices()


    # Step 5) Display all todo tasks and priorities to user
    if strChoices == "1":
        Outputs.DisplayList(listStruct)


    # Step 6) Add a new task and priority to the list
    elif strChoices == "2":
        newTask, newPriority = Inputs.InputNewTask()
        isTaskAdded = ProcessFile.AddTask(listStruct, newTask, newPriority)
        Outputs.AddTaskStatus(isTaskAdded, newTask, newPriority)


    # Step 7) Remove a task and priority from the list
    elif strChoices == "3":
        removeTask = Inputs.InputTaskToDelete()
        isTaskFound = ProcessFile.DeleteTask(listStruct, removeTask)
        Outputs.DeleteTaskStatus(isTaskFound, removeTask)


    # Step 8) Save tasks and priorities to the ToDo.txt file
    elif strChoices == "4":
        isFileSaved = ProcessFile.SaveFile(fileName, listStruct)
        Outputs.FileSavedStatus(isFileSaved)


    # Step 9) Exit program
    elif strChoices == "5":
        Outputs.ExitMenu()
        break


    #Step 10) Default
    else:
        Outputs.Default()