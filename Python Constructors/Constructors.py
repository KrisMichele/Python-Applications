
#Data-----------------------------------------------
objFile = None #File Handle
strUserInput = None #A string which holds user input

class ProductData(object):
    listData = None
    # --Constructor--
    def __init__(self, listData=[]):
        self.__listData = listData

    def ToString(self, strData=""):
        for row in self.__listData:
            strLine = (str(row)).strip("[]")
            strData += strLine + "\n"
        return strData



#Processing-----------------------------------------
class ProductDataProcessor():

    def ProcessData(self, File):
        list = []
        instructionsObject = IO()
        instructionsObject.Instructions()
        try:
            File.seek(0)
            for line in File:
                list.append(str(line).strip("\n"))
            while (True):
                menuPromptObject = IO()
                strUserInput = menuPromptObject.MenuPrompt()
                if (strUserInput == "exit"): break
                else: list.append(strUserInput)
            ListObject = ProductData(list)
            File.seek(0)
            File.write(ListObject.ToString())
        except Exception as e:
            print("Error: " + str(e))


#IO ----------------------------------------------
class IO():
    def DisplayFileData(self, File, Message="Contents of File"):
        print(Message)
        try:
            File.seek(0)
            print(File.read())
        except Exception as e:
            print("Error: " + str(e))

    def Instructions(self):
        print("Type in a Product Id, Name, and Price you want to add to the file")
        print("(Enter 'Exit' to quit!)")

    def MenuPrompt(self):
        strUserInput = input("Enter the Id, Name, and Price (example: 1,ProductA,9.99): ")
        return strUserInput



#Main Method-----------------------------------------

#Object Creation:
DataProcessor = ProductDataProcessor()
IOObject = IO()

#Call Methods using Objects:
try:
    objFile = open("C:\_PythonClass\Module 8\Products.txt", "r+")
    IOObject.DisplayFileData(objFile, "Here is the current data:")
    DataProcessor.ProcessData(objFile)
    IOObject.DisplayFileData(objFile, "Here is this data was saved:")
except FileNotFoundError as e:
     print("Error: " + str(e) + "\n Please check the file name")
except Exception as e:
    print("Error: " + str(e))
finally:
  if(objFile != None):objFile.close()