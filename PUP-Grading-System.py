# greetings to the user
print ("\nWelcome to PUP Grading System!")

# asks for input
userGrade = float(input("\nPlease enter your grade percentage: "))
roundedGrade = round(userGrade)

# 1.0 to 1.75
if roundedGrade >= 97 and roundedGrade <= 100:
    print ("\nThis is the result based on your grade percentage \nGrade: 1.0 \nDescription: Excellent! \n")
elif roundedGrade >= 94 and roundedGrade <= 96:
    print ("\nThis is the result based on your grade percentage \nGrade: 1.25 \nDescription: Excellent! \n")
elif roundedGrade >= 91 and roundedGrade <= 93:
    print ("\nThis is the result based on your grade percentage \nGrade: 1.5 \nDescription: Very Good! \n")
elif roundedGrade >= 88 and roundedGrade <= 90:
    print ("\nThis is the result based on your grade percentage \nGrade: 1.75 \nDescription: Very Good! \n")

# 2.0 to 2.75
elif roundedGrade >= 85 and roundedGrade <= 87:
    print ("\nThis is the result based on your grade percentage \nGrade: 2.0 \nDescription: Good \n")
elif roundedGrade >= 82 and roundedGrade <= 84:
    print ("\nThis is the result based on your grade percentage \nGrade: 2.25 \nDescription: Good \n")
elif roundedGrade >= 79 and roundedGrade <= 81:
    print ("\nThis is the result based on your grade percentage \nGrade: 2.5 \nDescription: Satisfactory \n")
elif roundedGrade >= 76 and roundedGrade <= 78:
    print ("\nThis is the result based on your grade percentage \nGrade: 2.75 \nDescription: Satisfactory \n")