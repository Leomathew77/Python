# nested loop

for i in range(1,6):
    for j in range(1,6):
        for k in range(1,6):
            print(i,j,k)


# print *
#       * *
#       * * *
#       * * * *
#       * * * * *

for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()



# Reverse 


# for i in range(5,0,-1):
#     for j in range(i):
#         print("*", end="")
#     print()


# traingle

for i in range(1,6):
    for j in range(6-i):
        print(" ", end="")
    for k in range(1,i+1):
        print("* " , end="")
    print()


# print chess board pattern

for i in range(8):
    for j in range(8):
        if((i+j)%2 == 0):
            print("w", end=(" "))
        else:
            print("B", end=(" "))
    print()
         

n = "APPLE"

for i in range(1, len(n) + 1):
    for j in range(i):
        print(n[j], end=" ")    #Print the character stored at index j.
    print() 
