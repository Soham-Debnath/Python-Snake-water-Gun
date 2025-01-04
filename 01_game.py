# Snake water game
'''
1 for Snake
-1 for water
0 for Gun
'''
import random 
computer = random.choice([1,-1,0])
youstr=input("enter your choice b/w s, w, g : ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}

you = youDict[youstr]

print(f"Your choice {reverseDict[you]}\nComputer's choice {reverseDict[computer]}")

# Now we have 2 numbers/variables i.e. computer and you.

if (computer == you):
    print("Its a draw.")
else:
    if (computer == 1 and you ==-1):
        print("You Lose!")
    elif (computer == 1 and you ==0):
        print("You Win!")
    elif (computer == 0 and you ==-1):
        print("You Win!")
    elif (computer == 0 and you ==1):
        print("You Lose!")
    elif (computer == -1 and you ==1):
        print("You Win!")
    elif (computer == -1 and you ==0):
        print("You Lose!")
    else:
        print("something went wrong!")
