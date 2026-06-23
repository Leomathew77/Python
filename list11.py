# list

# collection of data 

a = [2,4,6,7,8,9,12,14,15]
# properties

# 1.list can have any element of any size

data = [1,2,3,"mohan",True,[12,13,14,15]]

# 2. lists are ordered

# a = [1,2,3,4]
# b = [3,1,2,4]

# print (a == b)

# 3. lists are indexed


  #   0  1  2  3  4  5  6  7  8  9
# a = [10,11,12,13,14,15,16,17,18,19]

# print(a)
# print(a[1])
# print(a[4:8])
# print(a[0:9:2])
# print(a[: :-1])
# print(a[: :])
# print(a[0:7])

# [start:stop:step]


# a = 'mohan das'
# print(a[2])
# print(a[5])

# 4.lists are mutable
# str immutable

# a=[11,12,13,14,15]
# a[0]="mohan"
# print(a)

# b = "mohan"
# b[0]="h"
# print(b)

#5. lists are dynamic

a=[11,12,13,14,15,16,17]
a[0:4]=[31,32,33,34,35,36]
print(a)


b = [31, 32, 33, 34, 35, 36, 15, 16, 17]
b[5:6] = ["mohan"]
print(b)

# 6. lists are nested

a = [11,12,[100,200],13,14,15]
# print(a[2][0])
b = a[2]
print(b[0])



a = [11,12,13,[100,200],14,15]
print(a[3][1])




# inbuilt methods in lists

# to add elements


# append(elements)
# add an elememnt to the end of the list

a = [11,12,13,14,15]
a.append(100)
a.append(200)
print(a) 

# extend() add an itreble to the list  

a = [11,12,13,14,15]
a.extend([31,32,33,"mohan"])
# a.extend("leo")
print(a)

# insert(index,value)

a = [11,12,13,14,15]
a.insert(1,"mohan")
print(a)


# to remove elements

# remove()
# pop()


a = [11,12,13,14,15,11,11,11,11,11]
a.remove(11)
print(a)

# pop() - removes the last element from the list 
# pop(index)

a = [11,12,13,14,17,18,12,132,154,25]
# a.pop()
# a.pop()
a.pop(0)
a.pop(0)
print(a)


# tuple

# collection of data
a = (2,3,1,"mohan",673,32,2,23)
# ordered
# indexed
# immutable

# a = (1,2,3,4)
# a[0] = 10
# print(a)


# ittretion
 

# a = [11,12,13,14,15]
# b = "mohan das"
# c = (100,200,300,400,500)

# # for i in a:
# # for i in b:
# # for i in c:
#     print(i)

a = "mohan"
# print(a[0])
print(len(a))

for i in range(0,len(a)):
    print(i,a[i])


fruits = ["apple","banana","watermelon","pineapple","orange","mango"]

for i in range(0,len(fruits)):
    print(i,fruits[i])



# amstrong number
# prime number

# num = int(input("Enter a number: "))

# temp = num
# count = 0

# # Count the digits
# while temp > 0:
#     count = count + 1
#     temp = temp // 10

# temp = num
# sum = 0

# # Check Armstrong
# while temp > 0:
#     digit = temp % 10
#     sum = sum + (digit ** count)
#     temp = temp // 10

# if sum == num:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")






# num = int(input("Enter a number: "))

# count = 0

# for i in range(1, num + 1):
#     if num % i == 0:
#         count += 1

# if count == 2:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")


# # find vowels and their position in a string

# name = input("Enter your name: ")

# for i in range(0,len(name)):
#     # print(i,a[i])
#     if name[i] == "a" or name[i] == "e" or name[i] == "i" or name[i] == "o" or name[i] == "u":
#         print(i,name[i])

# # in operator membership operator

# name = input("Enter a name: ")
# # vowel = "aeiou"

# for i in range(0,len(name)):
#     if name[i] in "aeiou":
#         print(i,name[i])

# # create a list of even numbers and odd numbers from first 100 number


# num=[]
# even=[]
# odd=[]

# for i in range(1, 101):
#     num.append(i)
# for i in num :
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(even)
# print(odd)


# # remove duplicates from this list

# c = [1,2,3,4,1,3,4,2,7,8,9,2,3,4,5]
# b = []
# for i in c:
#     if i not in b:
#         b.append(i)
# print(b)


# # break continue pass

# # pass
# age = 0
# if age >= 18:
#     pass
# b = 10
# print(b)

# # break
# for i in range (1,11):
#     if i == 6:
#         break
#     print(i)              #output: 1,2,3,4,5

# # continue
# for i in range (1,11):
#     if i == 6:
#         continue
#     print(i)             #output: 1,2,3,4,5,7,8,9,10




# prime number

# num=int(input('enter your number: '))
# prime = True
# if num == 1:
#     prime == False
# else:
#     for i in range(2,6):
#         if num % i == 0:
#             print("not a prime number")
#             break
#     else:
#             print("prime number")


# Input n words and make it into a sentence

n = int(input("Enter the number of words: "))

sen = ""

for i in range(n):
    words = input("Enter words: ")
    sen = sen + words + " "

print("sentence: ", sen)

# Reverse a string without using [::-1]

str = input("Enter a string: ")

rev =""

for i in range(len(str) -1,-1,-1):
    rev = rev + str[i]

print("Reversed string:", rev)



# a = "hello my name is kumar"
# b = a.split()
# print(b)


a = "hello my name is kumar"

words=[]
word=(" ")

for i in a:
    if i != " ":
        word = word + i
    else:
        words.append(word)
        word = " "
words.append(word)
print(words)










