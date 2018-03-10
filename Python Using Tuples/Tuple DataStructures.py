'''
Create new program that asks the user for the name of a household item,
and then asks for its estimated value. (This project is similar to the last one!):
1. Create empty tuple called 'table'.
2. Ask the user for new entries and stores them in the 2-dimensional Tuple.
3. Ask the user if they would like to save the data to a text file called HomeInventory.txt.
4. Determine if the file is empty. If it is, record header information
5. Write the tuple contents to the txt file in the form of a string.
'''

#1. Create empty tuple called 'table'.
table = ()

#2. Ask the user for new entries and stores them in the 2-dimensional Tuple.
while(True):

    #specify menu choice
    intChoice = int(input("Enter '1' if you want to enter an item into the inventory and '2' if you want to exit the menu:"))
    if intChoice == 1:

        #get the user input for an inventory item name and price
        strItemName = input("Enter in the item name:")
        floatItemPrice = float(input("Enter in the item price:"))

        #store into a new tuple called table:
        tplrow = (strItemName, floatItemPrice)
        table += tplrow,

    elif intChoice == 2:
        print("You are exiting the database now.")
        break  # break out of the while loop if you want to exit the menu

    else:
        # provide a default case in the event the user did not enter in the correct information
        print("You did not enter a valid choice. Please enter either 1 or 2.")



#3. Ask the user if they would like to save the data to a text file called HomeInventory.txt.
strChoice = input("Would you like to save all your entered data into the Home Inventory Database?(y/n)")

if strChoice.lower() == "y":
    #4. Determine if the file is empty. If it is, record header information:
    file = open("C:\\Users\\Kristen\\Dropbox\\Python Foundations\\Module04\\Homework\\Assignment04\\HomeInventory.txt", "r+")
    filecontents = file.read()
    if not filecontents:
        file.writelines("Item ID , Item Price")
    file.close()

    #5. Write the tuple contents to the txt file in the form of a string.
    file = open("C:\\Users\\Kristen\\Dropbox\\Python Foundations\\Module04\\Homework\\Assignment04\\HomeInventory.txt", "a")
    for row in table:
        file.write("\n{} , {} ".format(row[0], row[1]))
    file.close()

else: print("No data was stored in the database.")
