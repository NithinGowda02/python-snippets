import random

while True:
    com_num1 = random.randint(1,6)
    com_num2 = random.randint(1,6)
    user_choice = input("Roll the dice? (y/n) >> ").lower()
    if user_choice == 'y':
        print(f"({com_num1}, {com_num2})")
        continue
    elif user_choice == 'n':
        print("Thanks for playing!") 
        break
    else:
        print("Invalid choice")    