#-----------------------------------if-elif-else-------------------------------------
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are now signed up!")
# elif age < 0:
#     print("You haven't been born yet!")    
# else: 
#     print("You must be 18+ to sign up!")    



# mark = 70
# if mark >= 40:
#     print("Passed")
# elif mark < 18:
#     print("Critical stage")
# else: 
#     print("Failed")        



# units = 1499
# if units <= 200:
#     print("No charge")
# elif units >= 1000:
#     print("Bill = Rs.", units * 5)
# else:
#     print("Bill = Rs.", units * 10)   



# temp = float(input("Enter temperature in ℃: "))
# if temp > 30:
#     print("It's hot")
# elif temp >= 20:
#     print("Normal weather")
# else:
#     print("Cold")    


# marks = 60
# if marks <= 40:
#     print("Grade B")
# elif marks >= 50:
#     print("Grade A")
# else :
#     print("Grade C")         


#------------------------------------match-case(Python 3.10+)-----------------------------------
# day = "Friday"
# match day: 
#     case "Monday":
#         print("Start of the week")
#     case "Friday":
#         print("Almost weekend")
#     case _:
#         print("Other day")        



# a = int(input("Enter A: "))
# b = int(input("Enter B: "))
# op = input("Enter operator (+, -, *, /): ")

# match op:
#     case "+":
#         print("Sum =", a + b)
#     case "-":
#         print("Difference =", a - b)
#     case "*":
#         print("Product =", a * b)
#     case "/":
#         print("Division =", a / b)
#     case _:
#         print("Invalid operator")                



# grade = input("Enter grade (A/B/C/D): ")
# match grade: 
#     case "A":
#         print("Excellent")
#     case "B":
#         print("Good job")
#     case "C":
#         print("Need improvement")
#     case "D":
#         print("Failed")
#     case _:
#         print("Invalid grade")                



# choice = int(input("Enter your choice (1-3): "))
# match choice:
#     case 1:
#         print("You ordered Burger")
#     case 2:
#         print("You ordered Pizza")
#     case 3:
#         print("You ordered Sandwich")
#     case _:
#         print("Invalid Choice")            



# day = input("Enter day: ")
# match day: 
#     case "Saturday" | "Sunday":
#         print("Weekend")
#     case _:
#         print("Weekday")    



# vehicle = input("Enter vehicle (bus/train/taxi): ")
# match vehicle: 
#     case "bus":
#         print("Fare = Rs. 20")
#     case "train":
#         print("Fare = Rs. 50")
#     case "taxi":
#         print("Fare = Rs. 100")
#     case _:
#         print("Invalid vehicle")            


# dept = input("Enter department (ENT/Ortho/Cardio): ")
# match dept:
#     case "ENT":
#         print("Ear, Nose, Throat Specialist")
#     case "Ortho":
#         print("Bone Specialist")
#     case "Cardio":
#         print("Heart Specialist")
#     case _:
#         print("Unknown Department")            








