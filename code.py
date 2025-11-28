import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([1,-1,0]) #random.choice for choicing random no 
yourchoice = input("enter your choice:")
gamedict = {"s": 1, "w": -1, "g": 0}
revercedict = {1:"snake",-1:"water",0:"gun"}
you = gamedict[yourchoice]
# By now we have 2 numbers,you and computer 
print(f"you chose {revercedict[you]}\ncomputer chose {revercedict[computer]}")
if(computer==you):
    print("Its a draw")

else:
    if(computer==-1 and you==1):
        print("you won!")
    elif(computer==-1 and you==0):
        print("you lost!")
    elif(computer==1 and you==-1):
        print("you lost!")
    elif(computer==1 and you==0):
        print("you won!")
    elif(computer==0 and you==1):
        print("you lost!")
    elif(computer==0 and you==-1):
        print("you won!")
    else:
        print("something went wrong")
    
