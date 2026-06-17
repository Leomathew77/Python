# Logical operators

# and
# or
# not

# and operator

# True True True
# True False False
# False True False
# False False False

a = 7
b = 10

if a > 6 and b == 10:
    print("yes")


# or operator

# True True True
# True False True
# False True True
# False False False

a = 6
b = 9

if a == 6 or b > 11:
    print("yes")

if (a > 1 or b > 10) and (a == 5 or b == 9):
    print("yes")




# not operator

a = 10 
print(not a == 10)



# largest of 3 numbers

a = 10
b = 11
c = -100

if a > b and a > c:
    print("a is largest")
elif b > a and b > c:
    print("b is largest")
else:
    print("c is largest")





# check if a number is a multiple of 3 and 5

num = 15
if num % 5 == 0 and num % 3 == 0:
    print("number is a multiple of 3 and 5")
else:
    print("number is not a multiple of 3 and 5")