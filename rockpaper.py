import random
print("select your choice as below :")
print("click 0 for rock")
print("click 1 for paper")
print("click 2 for scissors")
user=int(input("Enter your choice "))
comp=random.randint(0,2)
print("The compuer choice is:")
print(comp)
if(user==comp):
    print("The game draws")
elif(user==0 and comp==2):
    print("You wins the game")
elif(user==2 and comp==0):
    print("You lose the game")
elif(user>comp and user<=2):
    print("You wins the game")
elif(comp>user and user<=2):
    print("You lose the game")
else:
    print("invalid choice you loose the game")
    
    