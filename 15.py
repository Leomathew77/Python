# # age calculator
# # bmi calculator

# birthyear= int(input("Enter your birthyear: "))
# y = int(input("Enter current year: "))
# age = lambda y: 2026-y
# print("age =", age(birthyear))



# weight = float(input("Enter your weight (kg): "))
# height = float(input("Enter your height  (m): "))

# bmi = weight / (height ** 2)

# print("BMI =" , bmi)

# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#     print("Normal weight")
# elif bmi < 30:
#     print("Over weight")
# else:
#     print("obese")





# reccursion

# 10 numbers

# def counttozero(n): #stub 
#     print(n)
#     if n == 0:
#         return
#     return counttozero(n-1)
# counttozero(10)

# sum

def sum(n): 
    if n == 0:
        return 0
    return n + sum(n-1)
print("sum =", sum(10))


# fact

def factorial(n): 
    if n == 1:
        return 1
    return n * factorial(n-1)
print("fact =", factorial(5)) 
    


# scope of variable
# scope - area in which it is recognised

# name = "robert" # global scope
# def myname():
#     name = "mohan" #local scope
#     def nickname():
#         name = "leo" 
#         print(name)
#     nickname()
# myname()


# L E G B 
# local enclosing global built in 

def add(a,b): 
    print("sum =", a+b)
add(3,4)


def name(n):
    print("Name: ", n)
name("Leo")

# modules
import math
print(math.sqrt(25))
print(math.factorial(5))
print(math.pi)

a = 6.3
print(math.floor(a))

# random
# time 

