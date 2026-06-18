

# sum of digits in a number

# num = int(input("Enter a Number:"))
# sum = 0

# while num > 0:
#     b = num % 10
#     sum = sum + b
#     num = num // 10
# print("sum of digits =", sum)



# # Reverse of a number

# num = int(input("Enter a number :"))
# rev = 0

# while num > 0:
#     d = num % 10
#     rev = rev * 10 + d
#     num = num // 10
# print("Reversed number :",rev)



#factorial of number

# num = int(input("Enter a number :"))
# fact = 1

# while num > 0:
#     fact = fact* num
#     num = num - 1
# print("factorial :",fact)



# for loop

# for i in range(2,7,2):
#     print(i)


# # sum of 100 numbers

# sum = 0

# for i in range(1, 101):
#     sum = sum + i
# print(sum) 

# # factorial of a number
# num = int(input("Enter a number: "))
# fact = 1

# for i in range(1,num + 1):
#     fact = fact * i
# print("Factorial :", fact)

# multiplication table of a number

num = int(input("Enter a number : "))

for i in range (1,11):
    print(f'{num} x {i} = {num * i}') 


# find the sum and average of n number

count = int(input("Enter num count: "))
sum = 0
for i in range(count):
    num = int(input("Enter the number: "))
    sum = sum + num
print(f"sum is {sum}")
print(f"average = {sum/count}")