# Q1
#Gather value to evaluate
#day = int(input("input a numerical number 1-7: "))
# Mon = 1
# tues = 2
# wens = 3
# thu = 4
# fri= 5
# sat = 6
# sun = 7
#
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wesnday")
# elif day == 4:
#     print("Thurday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print(f"The input value {day} isnt valid. Please enter a numerical number 1-7")
# Q3
# # input age to evaluate
# age = int(input("What is your age? "))
##If the person is 1 year old or less, he or she is an infant.
##If the person is older than 1 year, but younger than 13 years, he or she is a child.
##If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
##If the person is at least 20 years old, he or she is an adult.
# if age <= 12:
#     print("You are an infint")
# elif age > 1 and age < 13:
#     print("You are a child. ")
# elif age >= 13 and age < 20:
#     print("You are a teen. ")
# elif age >= 20:
#     print("You are an adult. ")
# Q5
# input mass
#mass = int(input("What is your mass? "))
#Conversion is weight = mass * 9.8
# weight = mass * 9.8
# #Evaluate weight
# if weight > 500:
#     print("Too heavy. ")
# elif weight < 100:
#     print("Too light")
# Q7
# List the primary colors
print("The primiry color are: Red, Blue, and Yellow ")
color1 = input("whats the first color would you like to mix? ")
color2 = input("whats the second color would you like to mix? ")

#When you mix red and blue, you get purple.
#When you mix red and yellow, you get orange.
#When you mix blue and yellow, you get green.
if color1 == "red" and color2 == "blue":
    print("You made purple!")
elif color1 == "red" and color2 == "yellow":
    print("You made orange!")
elif color1 == "blue" and color2 == "yellow":
    print("You made green!")
else:
    print("Please choise a primary color")