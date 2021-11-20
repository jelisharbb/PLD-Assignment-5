# print welcome remarks
print ("\nWelcome! This program can determine the lowest number among the three numbers that you would enter.")

# defined a function
def lowestOfTheThree(first, second, third):
    if first < second and first < third:
        print (f"\nThe lowest number among the three is {first}.\n")
    elif second < first and second < third:
        print (f"\nThe lowest number among the three is {second}.\n")
    else:
        print (f"\nThe lowest number among the three is {third}.\n")

# asks input from the user
firstNum = float(input("\nEnter a number: "))
secondNum = float(input("Enter another number: "))
thirdNum = float(input("Enter another number: "))

# calling out the defined function
lowestOfTheThree(firstNum, secondNum, thirdNum)