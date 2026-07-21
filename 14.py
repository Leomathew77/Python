
# a = [11,12,13,14,15,16,17,18,19,20]

# mid = len(a)//2

# first_half = a[:mid]
# second_half = a[mid:]

# print(first_half)
# print(second_half)



# a = [11,12,13,14,15,16,17,18,19,20]

# b = a[:5] + [a[-1]]
# c = a[5:-1]

# print(b)
# print(c)

a = [11,1,100,-900,10,15,16]

# print("Largest=", max(a))
# print("smallest=", min(a))

largest = 0
smallest = 0

for i in a:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
print(largest,smallest)


# fuctions


# block of code which is executed which it is called


# def functionname(<arguments>):
    # code to be executed

def hello():
    print("hello good afternoon!!!")
hello()

# structural programming
# funtional  programming
# procedural programming

# arguments - values to be passed to a function

def add2(a,b):  #former parameter
    print(a + b)

add2(1,3)      #actual parameter
add2(14,27)       

# types of arguments
# 1. positional arguments
def add2(a,b):
    print(a+b)

add2(16,13)

# 2.keyword arguments

def fullname(fname,mname,lname):
    print(fname+''+mname+''+lname)

fullname(lname='jr' ,mname='downey' ,fname='Robert')

# return statement
# scope/

def add2(a,b):
     return 1,"mohan"
#  add2(a,b) == a+b
print(add2(1,4))


