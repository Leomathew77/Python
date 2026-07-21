#reccursion





# # def counttozero(n): #stub
# #     print(n)
# #     if n == 0:
# #         return
# #     return counttozero(n-1)

# # counttozero(10)

# # counttozero(10) = counttozero(9) = counttozero(8) = counttozero(7) = counttozero(6) = counttozero(5) = counttozero(4) = counttozero(3) = counttozero(2) = counttozero(1) = counttozero(0)

# #10 numbers

# def sumofn(n):
#     if n == 0:
#         return 0
#     return n + sumofn(n-1) 

# print(sumofn(10)) # 10 + sumofn(9) = 10 + 9 + sumofn(8) = 10 + 9 + 8 + sumofn(7) = 10 + 9 + 8 + 7 + sumofn(6) = 10 + 9 + 8 + 7 + 6 + sumofn(5) = 10 + 9 + 8 + 7 + 6 + 5 + sumofn(4) = 10 + 9 + 8 + 7 + 6 + 5 + 4 + sumofn(3) = 10 + 9 + 8 + 7 + 6 + 5 + 4 +3+ sumofn(2) = 10+9+8+7+6+5+4+3+2+sumofn(1)=10+9+8+7+6+5+4+3+2+1=55


# # factorial of a number
# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)

# print(fact(5)) 



#scope of a variable

# # scope - area in which it is recognized
# # name = "abhishek" #globaal variable
# # def myname():
# #     name = "leo"  #local variable
# #     def nickname():
# #         name ="yazil" #enclosing
# #         print(name)
# #     nickname()
# # myname()        





# #modules



# import math
# print(math.sqrt(25))
# print(math.factorial(5))
# print(math.pi)


# a = 6.3
# print(math.floor(a))

#random
import random
# print(random.randint(1,10))

# fruits = ["apple","orange,","pinapple","grapes","mango","watermelon"]
# print(random.choice(fruits))


# coin = ["heads","tales"]
# print(random.choice(coin))
    #  or

# coin = random.randint(0,1)
# if coin == 1:
#     print("heads")
# else:
#     print("tails")    



# rock,paper,scissors
# z = ["rock","paper","scissor"]
# computer = random.choice(z)
# user = ""
# while user not in z:
#     user = input("enter your choice rock/papper/scissor :-").lower()
# print(f"user : - {user} \ncomputer :-{computer}") 
# if user == computer:
#     print("tie!!!")
# elif user == "rock":
#     if computer == "scissor":
#         print("computer choice:",computer)
#         print("computer wins")
#     else:
#         print("user wins")    
# elif user == "paper":
#     if computer == "scissor":
#         print("computer choice:",computer)
#         print("computer wins")
#     else:
#         print("user wins")
# elif user == "scissor":
#     if computer == "rock":
#         print("computer choice",computer)
#         print("computer wins")
#     else:
#         print("user wins")    


# create an rpg game
# player  vs enemy


player = input("enter your name: -").lower()
enemy = random.choice(["dragon","goblin","hyper"])
playerhp = 100
enemyhp = 100
turn = 1
while playerhp > 0 and enemyhp > 0:
    print(f"Turn {turn}")
    print(f"{enemy} attacks player")
    playerhp = playerhp - random.randint(5,20)
    print(f"player hp is {playerhp}") 
    print("player attacks")   
    enemyhp = enemyhp - random.randint(5,20)
    turn = turn+1
    if playerhp <= 0:
        print(f"{enemy} won")
        break
    elif enemyhp <= 0:
        print(f"{player} won")
        break
           











#time
#os

