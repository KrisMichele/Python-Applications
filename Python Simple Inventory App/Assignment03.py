'''
Create a new program that asks the user for the name of a household item,
and then asks for its estimated value. Store, both pieces of data in a text
file called, HomeInventory.txt
'''

#use a while loop to keep the menu prompt up for entering multiple items into the txt database
while(True):

    #specify menu choice
    intChoice = int(input("Enter '1' if you want to enter items into the inventory and '2' if you want to exit the database:"))

    #use an if-then loop to execute  different code, based on the menu choice
    if intChoice == 1:
        #enter in the inventory item name and price
        strItemName = input("Enter in the item name:")
        floatItemPrice = float(input("Enter in the item price:"))

        #open the file, write the item and price to it, and then close the file
        objFile = open("C:\\Users\\Kristen\\Dropbox\\Python Foundations\\Module03\\Assignment03\\HomeInventory.txt", "a")
        objFile.write("\nThe item is a {} and the price is ${}".format(strItemName, floatItemPrice))
        objFile.close()


    elif intChoice == 2:
        print("You are exiting the database now.")
        break #break out of the while loop if you want to exit the menu


    else:
        #provide a default case in the event the user did not enter in the correct information
        print("You did not enter a valid choice. Please enter either 1 or 2.")
