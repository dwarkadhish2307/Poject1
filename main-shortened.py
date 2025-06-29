import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([1, -1, 0])
youstr = input("Enter your choice:")
youDict = {"s":1, "w":-1, "g":0}
you = youDict[youstr]
reverseDict = {1:"snake", -1:"water", 0:"gun"}
# By now we have 2 numbers(variable),you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
'''
if(computer == -1 and you == 1):
    print("You win")
elif(computer == 1 and you == -1):
    print("You lose")
elif(computer == 0 and you == 1):
    print("You lose")
elif(computer == 0 and you == -1):
    print("You win")
elif(computer == 1 and you == 0):
    print("You win")
elif(computer == -1 and you == 0):
    print("You lose")
elif(computer == you):
    print("It's a tie")
else:
    print("something went wrong")

    The below logic is written on the basis of the value of computer - you
    '''
if((computer - you) == -1 or (computer - you) == 2):
    print("you lose!")
else:
    print("you win!")

