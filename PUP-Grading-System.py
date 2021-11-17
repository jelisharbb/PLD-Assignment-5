# greetings to the user
print ("\nWelcome to PUP Grading System!")

# asks for input 
userGrade = input("\nPlease enter your grade percentage: ")

# if the user entered an integer\decimal
if userGrade.isdigit() == True:
    roundedGrade = round(float(userGrade))

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

    # 3.0 and 5.0
    elif roundedGrade == 75:
      print ("\nThis is the result based on your grade percentage \nGrade: 3.0 \nDescription: Passing \n")
    elif roundedGrade >= 65 and roundedGrade <= 74:
      print ("\nThis is the result based on your grade percentage \nGrade: 5.0 \nDescription: Failure \n")
 
    # if the user inputs number beyond the scope of the grading system
    elif roundedGrade > 100:
      print ("\nOops! Seems like you entered an invalid number. Please enter a number within the scope of the PUP Grading System. \n")

    # incomplete or withdrawn or dropped
    elif roundedGrade < 65 and roundedGrade >= 0:
       print ("\nThis is the result based on your grade percentage \nGrade: None \nDescription: Incomplete\Withdrawn\Dropped \n")

# if the user entered a string
else:
    alternativeGrade = userGrade.title()
    # incomplete
    if userGrade == "Incomplete" or userGrade == "incomplete" or userGrade == "Inc." or userGrade == "inc." or userGrade == "Inc" or userGrade == "inc" or userGrade == "None" or userGrade == "none":
        print ("\nThis is the result based on your grade percentage \nGrade: None \nDescription: Incomplete \n")