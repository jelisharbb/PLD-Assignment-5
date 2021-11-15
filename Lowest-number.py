# print welcome remarks
print ("\nWelcome! This program can determine the lowest number among the three numbers that you would enter.")

# defined a function
def lowestOfTheThree(x, y, z):
    if x < y and x < z:
        print (f"\nThe lowest number among the three is {x}.\n")
    elif y < x and y < z:
        print (f"\nThe lowest number among the three is {y}.\n")
    else:
        print (f"\nThe lowest number among the three is {z}.\n")

# asks input from the user
x_ = float(input("\nEnter a number: "))
y_ = float(input("Enter another number: "))
z_ = float(input("Enter another number: "))

lowestOfTheThree(x_, y_, z_)