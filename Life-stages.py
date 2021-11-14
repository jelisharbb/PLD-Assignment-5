# print a welcome remark
print ("\nGreetings! This program will determine if you are a kid, teen, debutant, or an adult based on the age that you will provide.")

# ask input from the user
userAge = int(input("\nPlease enter your age: "))

# if else conditions
if userAge >= 0 and userAge <= 12:
    print ("Hi! You're a kid. \n")
elif userAge >= 13 and userAge <= 17:
    print ("Hi! You're a teen. \n")
elif userAge ==18:
    print ("Hi! You're a debutant. \n")
elif userAge >= 19 and userAge <= 45:
    print ("Hi! You're an early adult. \n")
elif userAge >= 46 and userAge <= 65:
    print ("Hi! You're a middle adult. \n")
elif userAge >= 66 and userAge <= 120:
    print ("Hi! You're a late adult. \n")



