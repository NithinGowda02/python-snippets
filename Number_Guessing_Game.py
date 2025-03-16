import random
Number_list = []
for i in range(1,21):
    Number_list.append(i)
Actual_Number = random.choice(Number_list)
Chances = 1
print("You have 3 chances to guess the correct number.".upper())
while Chances <=3:
    print(f"CHANCE NUMBER >> {Chances}")
    User_Guess = input("Guess the number between (1 to 20) >> ")
    if User_Guess.isdigit():
        User_Guess = int(User_Guess)
        if User_Guess >= 1 and User_Guess <=20:
            print("Your number has been taken for process..!")
        else:
            print("Inavlid input try again with (1-20)")
    else:
        print("Invalid input try again with Numbers..") 


    if User_Guess == Actual_Number:
        print(f"Your Number >> {User_Guess} = Computer Number >> {Actual_Number}")
        print("Congratualations you guessed the Correct Number..")
        print("Thankyou for Participating in this Game..")
        break    
    elif User_Guess > Actual_Number:
        print(f"Your number is too Large >> {User_Guess}")
    elif User_Guess < Actual_Number:
        print(f"Your number is too Small >> {User_Guess}") 
    else:
        print("Thank you for Participation")
    Chances += 1
if Chances>3:
    print("Thank you for Participation..! You LOST")                             

