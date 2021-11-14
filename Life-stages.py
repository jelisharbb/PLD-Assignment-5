# print a welcome remark
print ("\nGreetings! This program will determine if you are a kid, teen, debutant, or an adult based on the age that you will provide.")

# ask input from the user
userAge = int(input("\nPlease enter your age: "))

# if else conditions
if userAge >= 0 and userAge <= 12:
    print ("Hi. You're a kid. \n")
elif userAge >= 13 and userAge <= 17:
    print ("Hi. You're a teen. \n")