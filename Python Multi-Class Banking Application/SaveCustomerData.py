#------------------------------------------------------------#
# Title: CustomerChecking.py
# Dev:   Kristen Yang
# Date:  12Mar18
# Desc: This application saves customer data to the text file
# ChangeLog: (Who, When, What) KY, 12Mar18, Initial Version
#------------------------------------------------------------#

if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")

class File(object):
    # --Constructor--
    def __init__(self, FileName="", Data=""):
        self.__FileName = FileName
        self.__Data = Data

    # --Properties--
    @property
    def FileName(self):
        return self.__FileName

    @FileName.setter
    def FileName(self, Value):
        self.__FileName = Value

    @property
    def Data(self):
        return self.__Data

    @Data.setter
    def Data(self, Value):
        self.__Data = Value

    # --Methods--
    def SaveData(self):
        """Writes data"""
        try:
            objFile = open(self.FileName, "a")
            objFile.write(self.Data)
            objFile.close()
        except Exception as e:
            print("Python reported the following error: " + str(e))
        return "Data Saved"

    def GetData(self):
        """Reads data"""
        try:
            objFile = open(self.FileName, "r")
            self.Data = objFile.read()
            objFile.close()
        except Exception as e:
            print("Python reported the following error: " + str(e))
        return self.Data

# ----------------end of class--------------------#