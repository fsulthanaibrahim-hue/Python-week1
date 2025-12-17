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














