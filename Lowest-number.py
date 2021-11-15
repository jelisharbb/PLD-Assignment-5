# print welcome remarks
print ("\nWelcome! This program can determine the lowest number among the three numbers that you would enter.")

def lowestOfTheTwo (x, y, z):
    lowest = x
    print (f"The lowest number among the three is {x}.")
    if y < lowest:
        lowest = y
        print (f"The lowest number among the three is {y}.")
    else:
        lowest = z
        print (f"The lowest number among the three is {z}.")