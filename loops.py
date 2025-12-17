#--------------------------for loop--------------------------------
# for i in range(5):
#     print("Hello")

#--------------------------for loop with string---------------------------
# for letter in "Python":
#     print(letter)


#--------------------------for loop with list-----------------------
# fruits = ["apple", "mango", "banana"]
# for f in fruits:
#     print(f)


#--------------------------while loop-----------------------------
# count = 1
# while count <= 3:
#     print("Count", count)
#     count += 1



# count = 2
# while count <= 5:
#     print("Count", count)
#     count += 1


# count = 1
# while count <= 5:
#     print("Count", count)
#     count += 2



#------------------------------------Break--------------------------------
# for x in range(10):
#     if x == 4:
#         break
#     print(x)


#----------------------------------Continue-----------------------------
# for x in range(5):
#     if x == 2:
#         continue
#     print(x) 



#----------------------------------Loop Else--------------------------------------
# for x in range(3):
#     print(x)
# else:
#     print("Loop completed")    



#------------------------------------List Loop----------------------------------------
# number = [10, 20, 30]
# for x in number:
#     print(x)



#-------------------------------------Tuple Loop--------------------------------------
# points = (3, 6, 9)
# for p in points:
#     print(p)



#-------------------------------------Set Loop-------------------------------
# names = { "Udaifa", "Hasna", "Wafa" }
# for n in names:
#     print(n)



#-------------------------------Dictionary Loop------------------------------
# student = { "name" : "Sulthana", "age" : 19 }
# for key in student:
#     print(key, student[key])




#------------------------Loops-------------------------------------
#==========for loop==========================
# fruits = ["Apple", "Orange", "Banana", "Cherry", "Peach", "Watermelon", "Mango", "Strawberry", "Pineapple", "Kiwi"]

# print("Apple")
# print("Orange")
# print("Banana")
# print("Cherry")
# print("Peach")
# print("Watermelon")
# print("Mango")
# print("Strawberry")
# print("Pineapple")
# print("Kiwi")


# fruits = ["Apple", "Orange", "Banana", "Cherry", "Peach", "Watermelon", "Mango", "Strawberry", "Pineapple", "Kiwi"]
# for fruit in fruits:
#     print(fruit)


# fruits = ["Apple", "Orange", "Banana", "Cherry", "Peach", "Watermelon", "Mango", "Strawberry", "Pineapple", "Kiwi"]
# for i in fruits:
#     print(i)


# fruit = "Apple"
# for i in fruit:
#     print(i)



#------------------------------------------------TASK----------------------------------------------
# Q1:
# Print numbers from 1 to 10
# condition1: numbers less than 5 --Number is less than 5
# condition2: numbers greater than or equal to 5 --Print that number
# Ans:-
# numbers = range(1, 11)
# for num in numbers:
#     if num < 5:
#         print("number is less than 5")
#     else:
#         print(num)    



# Q2:
# test_scores = [20, 50, 60, 14, 65]
# pass_mark = 40
# for score in test_scores:
#     if score < pass_mark:
#         print("Fail")
#     else:
#         print("Pass")    
# print("Completed")





# ========================while loop=======================
# status = ""
# while status != "delivered":
#     status = input("Update biriyani delivery status :")
# print("Yess! The biriyani has arrived")    


# response = "" 
# while response != "yes":
#     response = input("Type yes to continue : ")
# print("You typed yes")


# count = 0
# while count <= 5:
#     print(count)
#     count = count + 1




# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print(number)
# print(f"We have {count} even numbers")        