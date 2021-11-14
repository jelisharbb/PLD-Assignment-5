# greetings to the user
print ("\nWelcome to PUP Grading System!")

# asks for input
userGrade = float(input("\nPlease enter your grade percentage: "))
roundedGrade = round(userGrade)

# 1.0 to 1.75
if userGrade >= 97 and userGrade <= 100.:
    print ("\nThis is the result based on your grade percentage \nGrade: 1.0 \nDescription: Excellent! \n")
elif userGrade >= 94 and userGrade <= 96:
    print ("\nThis is the result based on your grade percentage \nGrade: 1.25 \nDescription: Excellent! \n")
elif userGrade >= 91 and userGrade <= 93:
    print ("\nThis is the result based on your grade percentage \nGrade: 1.5 \nDescription: Very Good! \n")
elif userGrade >= 88 and userGrade <= 90:
    print ("\nThis is the result based on your grade percentage \nGrade: 1.75 \nDescription: Very Good! \n")