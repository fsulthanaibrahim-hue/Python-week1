"""given number is prime or not"""
# num = int(input("Enter a number: "))
# if num <= 1:
#     print("Not a Prime number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a Prime number") 
#             break
#         else: 
#             print("Prime number")   


"""list with only even numbers using list comprehension"""
# def even_numbers(nums):
#     even_nums  = [num for num in nums if num % 2 == 0]
#     return even_nums
# list = [1, 2, 3, 4, 5, 6]
# result = even_numbers(list)
# print(result)


""" maps each character in a string to its frequency"""
# text = "hello"
# char_freq = {}
# for char in text:
#     char_freq[char] = char_freq.get(char, 0) + 1
# print(char_freq)    


""" reverse a list without using built-in methods"""
# for i in range(5, 0, -1):
#     print(i)


# my_list = [1, 2, 3, 4, 5]
# for i in range(len(my_list)-1, -1, -1):
#     print(my_list[i])


"""match-case to print the day of the week based on user input (1-7)"""
# day = int(input("Enter a number (1-7): "))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid input! Please enter 1-7.")                      


"""list of numbers, remove all duplicates using a set"""
# numb = [1, 2, 2, 3, 4, 4, 5]
# unique_numb = list(set(numb))
# print(unique_numb)


"""loops through a dictionary and prints key-value pairs"""
# student = {
#     "name": "Sulthana",
#     "age": 19,
#     "city": "Payyanur"
# }
# for key, value in student.items():
#     print(key, ":", value)


"""tuple from a list and show that it is immutable using a try-except block"""
# list = [1, 2, 3]
# my_tuple = tuple(list)
# print(my_tuple)
# try: 
#     my_tuple[1] = 10
# except:
#     print("Tuple cannot be changed")    


"""Reverse a string using slicing without using reversed() or a loop"""
# text = "hello"
# print(text[::-1])


"""a number as positive, negative or zero using conditional statements"""
# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive number")
# elif num < 0:
#     print("Negative number")
# else:
#     print("Zero")        


"""Write a function that accepts any number of arguments and returns their sum"""
# def add(a, b):
#     return a + b
# print(add(2, 3))


"""lambda function that squares a number and use it inside map() to square all elements in a list"""
# numb = [1, 2, 3, 4, 5]
# squared = list(map(lambda x:x*x, numb))
# print(squared)


""" recursive function to compute the factorial of a number"""
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))


"""14. Create a custom module with a function that calculates the area of a circle and import it"""
# import circle
# print(circle.area(5))


"""handle division by zero using try-except-else-finally"""
# try:
#     result = 10/0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# else:
#     print("Result :", result)
# finally:
#     print("Program finished.") 


"""function inside another function and return it (closure example)"""
# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function
# add_five =  outer_function(5)
# print(add_five(10))


"""decorator that prints 'Function started' before calling a function and 'Function ended' after"""
# def my_decorator(func):
#     def wrapper():
#         print("Function started")
#         func()
#         print("Function ended")
#     return wrapper
# @my_decorator
# def say_hello():
#     print("Hello")
# say_hello()        


"""generator function to yield squares of numbers from 1 to n"""
# def squares(n):
#     for i in range(1, n+1):
#         yield i*i
# for x in squares(3):
#     print(x)        


"""dictionary with the number as the key and its square as the value (dict comprehension)"""
# numbers = [1, 2, 3, 4, 5]
# result = {n: n*n for n in numbers}
# print(result)


"""a sentence and outputs the words in alphabetical order"""
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# words.sort()    
# print(words)


"""merge two dictionaries into one"""
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# dict1.update(dict2)
# print(dict1)


"""counts how many times each vowel appears in a given string"""
# text = "Python is easy"
# text = text.lower()
# vowels = "aeiou"
# for vowel in vowels:
#     count = text.count(vowel)
#     print(vowel, ":", count)


"""if a given string is a palindrome (case-insensitive)"""
# text = "madam"
# text = text.replace(" ", "")
# if text == text[::-1]:
#     print("Pallindrome")
# else:    
#     print("Not a pallindrome")




"""Mini project"""
###"""Basic Calculator"""

# while True:
#     print("Enter operation (+, -, *, /) or 'exit' to quit:")
#     op = input()
#     if op == "exit":
#         break
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     if op == "+":
#         print("Result:", num1 + num2)
#     elif op == "-":
#         print("Result:", num1 - num2)
#     elif op == "*":
#         print("Result:", num1 * num2)
#     elif op == "/":
#         if num2 != 0:
#             print("Result:", num1 / num2)
#         else:
#             print("Cannot divide by zero")
#     else:
#         print("Invalid operation")                        


###"""tores marks in a dictionary, calculates average, shows top scorer"""
# students = {
#     "Fathima": [80, 90, 85],
#     "Aysha": [70, 75, 80],
#     "Meharin": [90, 95, 92]
# }
# for name, marks in students.items():
#     avg = sum(marks)/len(marks)
#     print(f"{name} - average: {avg}")
# top_student = max(students, key=lambda x: sum(students[x]))
# print("Top student:", top_student)    



"""class BankAccount with deposit and withdraw methods and a balance attribute"""
# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount)
#         print("Balance:", self.balance)

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawn:", amount)
#             print("Balance:", self.balance)
#         else:
#             print("Insufficient balance")    
# account = BankAccount(1000)
# account.deposit(500)
# account.withdraw(300)
# account.withdraw(1500)


"""class Animal and inherit it in class Dog, overriding a method"""
# class Animal:
#     def speak(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")
# a = Animal()
# a.speak()
# d = Dog()
# d.speak()                
 








