name = input("Enter your name >> ")
print(f"hello {name.upper()} welcome to adventure game".upper())
print("=========================================================")
answer = input("You are on a dirt road, it has come to an end and you can go left or right >> ").lower()
if answer == "left":
    answer = input("You come river, you can walk around it or swim accross? type walk to walk around type swim to swim accross >> ")
    if answer == "swim":
        print("You swam accross and were eaten by an alligator!")
    elif answer == "walk":
        print("You walked for a miles, ran out of water you lost the game.!")

    else:
        print("Invalid choice. YOU LOSE!") 

elif answer == "right":
    answer = input("You come to bridge it look wobbly, do you want to cross it or head back (cross/back) >> ").lower()
    if answer == "back":
        print("You go back and lose.")   
    elif answer == "cross":
        answer=input("You cross the bridge and meet a stranger. Do you talk to them(yes/no) >> ").lower()
        if answer == "yes":
            print("You talk to the Stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("you ignored the stranger and they are offended and you lose.")
        else:
            print("Invalid choice. YOU LOSE!")  
    else:
        print("Invalid choice. YOU LOSE!") 
else:
    print("Invalid choice. YOU LOSE!") 

print("===========================================================")  
print(f"thank you for trying {name.upper()}".upper())      