#-----------------------------------------------------------------------------#
# Title: Module 7 - Assignment 07
# Dev:   Kristen Yang
# Date:  February 26, 2018
# Change Log: (revision number, Who, When, What)
#   Rev. 0 (Assignment 07), KY, 02/26/18, Create Script with Exception Handling
# References:
#1) Michael Dawson. Python Programming for the Absolute Beginner.
#   Third Edition, Chapter 7. Boston, MA: Course Technology, 2010.

#2) Randall Root. "Module 07 Programming Notes." (2018): all pages.
#    https://canvas.uw.edu/courses/1177874/files/44880387?module_item_id=7923725>

#3) Python Software Foundation, “Python 3.3.7 Documentation –
#   The Python Tutorial for Errors and Exceptions” (2017).
#   <https://docs.python.org/3.3/tutorial/errors.html>
#----------------------------------------------------------------------------#



#--- Declare Variables and Constants------------------------------------------#
"""
fileName is the filepath for Statistics.txt
listData is the list data structure used to hold float data entered by the user.
"""
FileName = "C:\\_PythonClass\\Module 7\\Statistics.txt"
listData = []



#-- Data Processing Class and Functions---------------------------------------#
class DataProcess(object):

    @staticmethod
    def AddToList(data, list):
        """
        This function checks to see that the data point input by the user
        is a float. If it is a float, the data is added to a list.
        :param data - The data point input by the user.
        :return list - The list data structure used to hold each data point input by the user.
        """
        if isinstance(data, float):
            list.append(data)
        return list

    @staticmethod
    def MeanCalc(list):
        """
        This function is used to calculate the mean of all data points within the list. If an error occurs
        during calculations (e.g., no data points were entered), the user will be notified of the error.
        :param list - The list data structure used to hold each data point input by the user.
        :param sum - The sum of all data points in the list.
        :return mean -  The average of all data points.
        """
        sum = 0
        try:
            for i in list:
                sum = sum + i
            mean = sum / len(list)
            return mean
        except ZeroDivisionError as e: print("\nCheck to see that at least one datapoint was entered.\
        \nThe following divide by zero error occurred during calculation of the mean:\n{}".format(e))
        except Exception as e: print(e)


    @staticmethod
    def StDevCalc(list, mean):
        """
        This function is used to calculate the standard deviation of all data points within the list.
        If an error occurs during calculations (e.g., only one data point was entered by the user),
        the user will be notified of the error.
        :param list - The list data structure used to hold each data point input by the user.
        :param mean - The average of all data points.
        :param squDiff - The square of each data point subtracted by the mean.
        :param sumSquDiff - The sum of all squDiff numbers.
        :param variance - The squared deviation of a random variable from its mean.
        :return stdev -  The standard deviation (amount of variation) within the data in list.
        """
        sumSquDiff = 0
        try:
            for i in list:
                squDiff = (i - mean) ** 2
                sumSquDiff = sumSquDiff + squDiff
            variance = sumSquDiff / (len(list) - 1)
            stdev = variance ** 0.5
            return stdev
        except ZeroDivisionError as e: print("\nCheck to see that at least two data points were entered. \
        \nThe following divide by zero error occurred during calculation of the standard deviation:\n{}".format(e))
        except Exception as e: print(e)


    @staticmethod
    def WriteFile(filePath, list, mean, stdev):
        """
        This function is used to append the Statistics.txt file with the user input
        list data, the calculated mean and the calculated standard deviation. If an error occurs during
        opening, appending, or closing the file, the user will be notified of the error.
        :param filePath - The filepath for Statistics.txt.
        :param file - The file at path filePath opened in append format.
        :param list - The list data structure used to hold each data point input by the user.
        :param mean - The average of all data points.
        :param stdev -  The standard deviation (amount of variation) within the data in list.
        :param strListData - The list data converted to a string to allow writing to Statistics.txt.
        :param strCalcData - The mean and standard deviation converted to a string to allow writing to Statistics.txt.
        """
        strListData = ("The data entered is:\n{}\n".format(list))
        strCalcData = ("The mean is: {} and standard deviation is: {}\n".format(mean, stdev))
        try:
            file = open(filePath, "a")
            file.writelines(strListData)
            file.writelines(strCalcData)
            file.writelines("\n")
            file.close()
        except IOError as e: print("\nI/O error is:\n{}".format(e))
        except Exception as e: print(e)



#-- Input / Output Class and Functions----------------------------------------#
class IO(object):

    @staticmethod
    def Instructions():
        """
        This function is used to display the general instructions for executing the script to the user.
        """
        print("Instructions:\n1)Enter in your sample data, one point at a time.\
        \n2)When all data is entered, type 'exit' to quit the menu and start the statistical analysis.\n")

    @staticmethod
    def UserChoice():
        """
        This function is used to display a menu prompt to the user and capture the user input.
        :return choice - A menu of user options used to capture the user input.
        """
        choice = input("Enter 'y' to continue entering data or type 'exit':")
        return choice

    @staticmethod
    def UserDataInput():
        """
        This function is used to capture the data point value input by the user and convert that data point to a float.
        If the data point cannot be converted, the user will be notified to enter a numeric data point
        :return data - The data point that is input by the user.
        """
        try:
            data = float(input("Enter a datapoint:"))
            return data
        except ValueError as e: print("\nA numeric datapoint must be entered. The following error occured:\n{}".format(e))


    @staticmethod
    def DefaultMessage():
        """
        This function is used to display a default message if the user selects an invalid menu choice.
        """
        print("\nYou did not enter a valid option. Please retry.")

    @staticmethod
    def DisplayData(list, mean, stdev):
        """
        This function is used to display the data the user entered, the calculated mean and the calculated standard
        deviation.
        :param list - The list data structure used to hold each data point input by the user.
        :param mean - The average of all data points.
        :param stdev -  The standard deviation (amount of variation) within the data in list.
        """
        print("\nYou entered in the following data:")
        print(list)
        print("The mean of the data is: {}".format(mean))
        print("The sample standard deviation of the data is: {}".format(stdev))
        print("The data will be saved in Statistics.txt at the following file path: C:\\_PythonClass\\Module 7")



#-- Main Method---------------------------------------------------------------#
#Step 1) Create Objects for each Class
processObject = DataProcess()
userObject = IO()

#Step 2) Display the Instructions to the User
userObject.Instructions()

#Step 3) Allow the User to Continuously Input Data or Exit the Menu When Complete.
while(True):
    strInput = userObject.UserChoice()
    if strInput == 'y':
        fltData = userObject.UserDataInput()
        listData = processObject.AddToList(fltData, listData)
    elif strInput.lower() == 'exit': break
    else: userObject.DefaultMessage()

#Step 4) Calculate the Mean
listMean = processObject.MeanCalc(listData)

#Step 5) Calculate the Standard Deviation
listStdev = processObject.StDevCalc(listData, listMean)

#Step 6) Display the Data and Calculations
userObject.DisplayData(listData, listMean, listStdev)

#Step 7) Write data to the File
processObject.WriteFile(FileName, listData, listMean, listStdev)


