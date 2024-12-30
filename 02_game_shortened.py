import random 
computer = random.choice([1,-1,0])
youstr=input("enter your choice b/w s, w, g : ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}

you = youDict[youstr]

print(f"Your choice {reverseDict[you]}\nComputer's choice {reverseDict[computer]}")

# Now we have two numbers/variables i.e. computer and you.

if (computer == you):
    print("Its a draw.")
else:
    if((computer - you)==-2 or (computer - you)==1):
        print("you win!")
    else:
        print("You Lose!")
'''
else:
    if (computer == 1 and you ==-1):       computer - you = 2
        print("You Lose!")
    elif (computer == 1 and you ==0):      computer - you = 1
        print("You Win!")
    elif (computer == 0 and you ==-1):     computer - you = 1
        print("You Win!")
    elif (computer == 0 and you ==1):      computer - you = -1
        print("You Lose!")
    elif (computer == -1 and you ==1):     computer - you = -2
        print("You Win!")
    elif (computer == -1 and you ==0):     computer - you = -1
        print("You Lose!")
    else:
        print("something went wrong!")

    You win only when (computer - you) = -2 or 1
'''

