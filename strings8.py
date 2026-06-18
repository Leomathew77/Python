# strings


# ''
# ""
# ''''''

name = "mohan"
print(name)
print(type(name))


data = "mohan's resume"
print(data)

qt='''gandhi once said that" Say no to violence " '''
print(qt)




# escape sequence

# \'------'
# \"------"
# \n - new line
# \t - tab space 
# \b - backspace  
# \\ - used to remove the escape sequence

data = 'mohan\'s resume'
print(data)
qt="gandhi once \t said that\n\" Say no to violence \""
print(qt)

# raw string
qt=r"gandhi once \t said that\n\" Say no to violence \""
print(qt)

# input function

# input()-----str 

# a = input(" Enter Your Name: ")
# print(a)


# Type conversion / casting

# implicit
# explicit

a = int(input(" Enter a number: "))
b = int(input(" Enter an other number: "))
print(a+b)


a = float(input(" Enter a number: "))
b = float(input(" Enter an other number: "))
print(a+b)


# String format 

name = "mohan"
age = 45
married_status = "false"
rating = 4.5

result = f"my name is {name}, my age is {age}, my married status is {married_status},my rating is {rating}"
print(result)