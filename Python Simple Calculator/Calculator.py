#Addition method with both integers passed into it
def Addition(intNum1, intNum2):
    intsum = intNum1 + intNum2
    print("-------------------------------------------")
    print("Addition of {} and {} is: {}".format(intNum1, intNum2, intsum))
    
"""
Subtraction method with both integers passed into it.
Two subtraction operations are conducted to show each number subtracted by the other
"""
def Subtraction(intNum1, intNum2):
    intdiff1 = intNum1 - intNum2
    intdiff2 = intNum2 - intNum1
    print("-------------------------------------------")
    print("Subtraction of {} from {} is: {}".format(intNum2, intNum1, intdiff1))
    print("-------------------------------------------")
    print("Subtraction of {} from {} is: {}".format(intNum1, intNum2, intdiff2))

#Multiplication method with both integers passed into it
def Multiplication(intNum1, intNum2):
    intmult = intNum1 * intNum2
    print("-------------------------------------------")
    print("Multiplication of {} and {} is: {}".format(intNum1, intNum2, intmult))

"""Division method with both integers passed into it.
#Two division operations are conducted to show each number divided by the other.
"""
def Division(intNum1, intNum2):

    intdiv1 = intNum1 / intNum2
    intdiv2 = intNum2 / intNum1
    print("-------------------------------------------")
    print("Division of {} by {} is: {}".format(intNum1, intNum2, intdiv1))
    print("-------------------------------------------")
    print("Division of {} by {} is: {}".format(intNum2, intNum1, intdiv2))
    print("-------------------------------------------")


"""
Start of the main method. The program first executes here,
and the user enters in two numbers. The numbers are converted
to integers from strings.
"""
intNum1 = int(input("Enter in the first number:"))
intNum2 = int(input("Enter in the second number:"))


"""
The methods for each operation are then called,
and the integers are passed into each method call
"""
Addition(intNum1, intNum2)
Subtraction(intNum1, intNum2)
Multiplication(intNum1, intNum2)
Division(intNum1, intNum2)
