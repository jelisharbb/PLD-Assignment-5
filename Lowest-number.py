# print welcome remarks
print ("\nWelcome! This program can determine the lowest number among the three numbers that you would enter.")

def lowestOfTheTwo(x, y, z):
    if x < y and x < z:
        print (f"\nThe lowest number among the three is {x}.\n")
    elif y < x and y < z:
        print (f"\nThe lowest number among the three is {y}.\n")
    else:
        print (f"\nThe lowest number among the three is {z}.\n")