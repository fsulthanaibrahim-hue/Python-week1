# print("Helllo")

# print("Hello " + "World")

# print("How are you")

# print("How are you!")

# print("Hai " + input("What is your name :"))

# name = input("Enter your name :")
# hobby = input("Enter your hobby :")
# print("I am " + name + " and " + "I love " + hobby)

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("My name is ", name)
# print("My age is ", age)


# print("Hello")
# str=input("Enter something: ")
# print("str")




#---------------------------------------Comments------------------------------------------
# My first comment -this is a python example
# Ith ayirikum print avan ullaa message
"""
Multi comment- ith python ignore cheyyum 
just explanation mathrm
"""
# print("Python Learning!")








#------------------------------------variables----------------------------------------

# name = "Fathima"
# age = 19
# print(name, age)

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# color = input("Enter your favourite color: ")
# print("My name is ", name)
# print("I am ", age ,"years old")
# print("My favorite color is ", color)







#####--------------------------------------Revision--------------------------------------------######
# print("Fathimath Sulthana")
# print("19 years old")
# print("I am learning python")

#-------------------------Variables-------------------------
# city = "Payyanur"
# print(city)

# price = 50
# print(price)

# price = 50
# print(price)
# price = 100
# print(price)



#--------------------------Store integer, float, string in variables--------------------------
# age = 20
# price = 99.5
# name = "Fathima"
# print(age)
# print(price)
# print(name)
# print(type(age))
# print(type(price))
# print(type(name))



####-----------------------------Operators--------------------------------------
##========================Arithemtic operators======================
# a = 10
# b = 3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)


###=========================Modulus operators=======================
# num = 10
# print(num % 2)


####======================Comparison operators=======================
# a = 5
# b = 10
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)


####======================Logical operators==========================
# x = 5
# print(x > 3 and x < 10)
# print(x > 3 or x < 2)
# print(not(x > 3))


#####-----------------------Conditionals-----------------------------
###===============if condition=====================
# num = int(input("Enter a number : "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")        


###=================match case===================
# day = int(input("Enter day number : "))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case _:
#         print("Invalid day")        


#####---------------------------------------Loops---------------------------------------
###================for loop==================
# for i in range(5):
#     print("Hello")


###=================while loop================
# i = 1
# while i <= 5:
#     print(5)
#     i = i + 1


# i = 1
# while i <= 3:
#     print("Python")
#     i += 1


###----------------------------Loop through a list-------------------------------
# nums = [1, 2, 3, 4]
# for n in nums:
#     print(n)


###---------------------------Print only even numbers from list--------------------------
# nums = [1, 2, 3, 4, 5, 6]
# for n in nums:
#     if n % 2 == 0:
#         print(n)



###------------------------Loop through string---------------------------
# name = "Python"
# for n in name:
#     print(n)


###-----------------------------Break--------------------------
# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)


###--------------------------Continue-----------------------------
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)


###------------------------------Create a list--------------------------------
# numbers = [10, 20, 30]
# print(numbers)


###----------------------------Access list element------------------------
# numbers = [10, 20, 30, 40]
# print(numbers[0])
# print(numbers[2])


###---------------------------Change list value----------------------
# numbers = [10, 20, 30]
# numbers[1] = 25
# print(numbers)


###--------------------------Add element to list---------------------------
# numbers = [1, 2, 3]
# numbers.append(4)
# print(numbers)


###----------------------------Loop through list-----------------------------
# fruits = ["apple", "banana", "mango"]
# for fruit in fruits:
#     print(fruit)


###-----------------------------Tuple-------------------------------
###-----------Create tuple------------------
# t = (10, 20, 30)
# print(t)


###----------------Access tuple element--------------
# t = (10, 20, 30)
# print(t[1])


###-----------------------------Set------------------------------------
###-----------Create set--------------------
# nums = {1, 2, 3, 3, 4}
# print(nums)


###----------Add element to set----------------
# nums = {1, 2, 3}
# nums.add(4)
# print(nums)


###----------Remove deuplicate from list-------------------
# numbers = [1, 2, 2, 3, 4, 4]
# unique = set(numbers)
# print(unique)



###-----------------------------------------Loop Dictionary---------------------------------------
# student = {
#     "name": "Ali",
#     "age": 20,
#     "city": "Payyanur"
# } 
# for key, value in student.items():
#     print(key, ":", value)



###-------------------------------------------Functions-------------------------------------------
##---------------Add 2 numbers----------------
# def add(a, b):
#     return a + b
# result = add(2, 3)
# print(result)


##--------------function + print inside------------------
# def greet():
#     print("Hello Python")
# greet()    


##-------------function with user input---------------------
# def add_numbers():
#     a = int(input("Enter first number : "))
#     b = int(input("Enter second number : "))
#     print("Sum : ", a + b)
# add_numbers()    


##--------------function with return-------------------
# def square(num):
#     return num * num
# result = square(4)
# print(result)


##--------------function with multiple arguments----------------
# def student(name, age):
#     print("Name :", name)
#     print("Age :", age)
# student("Fathima", 20)    


##---------------------------------Error Handling(try, except)------------------------------------------
##-------------try, except------------------
# try:
#     print(10/0)
# except:
#     print("Error occured")    


##--------------user input division--------------
# try:
#     a = int(input("Enter a number : "))
#     print(10 / a)
# except:
#     print("Cannot divide by zero")    


##-------------try, except, else, finally-------------------
# try:
#     a = 5
#     b = 1
#     print(a / b)
# except:
#     print("Error")
# else:
#     print("Division successfull")
# finally:
#     print("Program ended")            


###----------------------------------Strings...--------------------------------------
##------------find length of string-------------
# name = "Python"
# print(len(name))


##-------------access string characters--------------
# name = "Python"
# print(name[0])
# print(name[3])


##------------loop through string-------------------
# name = "Hi"
# for i in name:
#     print(i)


##-------------Reverse string using slicing------------------
# text = "hello"
# print(text[::-1])


##--------------Convert to uppercase/lowercase------------------
# name = "Python"
# print(name.upper())
# print(name.lower())


##----------------Check word inside string---------------------
# text = "Who are you ?"
# print("Python" in text)


##---------------Count vowels-------------------
# text = "hello"
# count = 0
# for i in text:
#     if i in "aeiou":
#         count += 1
# print("Vowels :", count)        




#####-------------------------------------------------Revision--------------------------------------------
"""even and odd"""
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# print("Even numbers : ")
# for i in nums:
#     if i % 2 == 0:
#         print(i)
# print("Odd numbers : ")
# for i in nums:
#     if i % 2 == 1:
#         print(i)

"""sum"""
# nums = [10, 20, 30, 40, 50]
# total = 0
# for i in nums:
#     total = total + i
# print("Sum :",total)    

"""revers"""
# text = "python"
# print(text[::-1])

"""vowels..."""
# word = "education"
# count = 0
# for i in word:
#     if i in "aeiou":
#         count = count + 1
# print("Vowels :", count)        


"""largest number"""
# numbers = [12, 45, 7, 89, 23]
# largest = numbers[0]
# for i in numbers:
#     if i > largest:
#         largest = i
# print("Largest :", largest)        

"""remove duplicates"""
# nums = [1, 2, 2, 3, 4, 4, 5]
# unique_nums = list(set(nums))
# print(unique_nums)


"""Loop through a dictionary and print key-value pairs"""
# student = {
#     "name": "Fathima",
#     "age" : 20,
#     "course" : "Python"
# }
# for key, value in student.items():
#     print(key, ":", value)


"""function to add 2 numbers"""
# def add(a, b):
#     return a + b
# result = add(10, 5)
# print(result)


"""last item print cheyyuka"""
# nums = [10, 20, 30, 40]
# print(nums[3])


"""change first value"""
# nums = [5, 10, 15]
# nums[0] = 50
# print(nums)

"""add item at end"""
# nums = [1, 2, 3]
# nums.append(4)
# print(nums)


"""add item at begining"""
# nums = [2, 3, 4]
# nums.insert(0, 1)
# print(nums)


"""remove last item"""
# nums = [10, 20, 30]
# nums.pop()
# print(nums)


"""print numbers greater than 10"""
# nums = [5, 12, 8, 20]
# for n in nums:
#     if n > 10:
#         print(n)


"""Count even numbers"""
# nums = [1, 2, 3, 4, 5, 6]
# count = 0
# for i in nums:
#     if i % 2 == 0:
#         count = count + 1
# print(count)         


"""Check list is empty"""
# nums = []
# if len(nums) == 0:
#     print("List is empty")
# else:
#     print("List is not empty")    


"""join list items"""
# letters = ["a", "b", "c"]
# result = "".join(letters)
# print(result)


"""print index of ("banana")"""
# fruits = ["apple", "banana", "mango"]
# print(fruits.index("banana"))











