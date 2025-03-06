import random
Rock="""
         ___
        |___)__
 ______/_______)
        _______)
 ______ _______)
       \_______)
        
"""
Paper="""
       ______
_______/_____)___
        _________)_
        ___________)
_______ __________)
        \________)
"""
Scissors="""
         ____
________/    |___________
                _________)
               <_________
                _________)
_________        ___)
         \__________)

"""
computer_won=0
User_won=0
i=0
while i<3:
    choice=[Rock,Paper,Scissors]
    comp_input=[0,1,2]
    com_choice=random.choice(comp_input)
    user_input=int(input("""
                         Rock : 0
                         Paper : 1
                         Scissor : 2
                         Enter the your choice >> """))
    if com_choice==user_input:
        print(f"COMPUTER CHOICE >>>\n{choice[com_choice]} YOUR CHOICE >>>{choice[user_input]} Its a DRAW Match...")
    elif com_choice==0 and user_input==2:
        print(f"COMPUTER CHOICE >>>\n{choice[com_choice]} YOUR CHOICE >>>{choice[user_input]} You LOST...")
        computer_won+=1  
    elif com_choice==2 and user_input==0:
        print(f"COMPUTER CHOICE >>>\n{choice[com_choice]} YOUR CHOICE >>>{choice[user_input]} You WON...")
        User_won+=1   
    elif user_input>com_choice:
        print(f"COMPUTER CHOICE >>>\n{choice[com_choice]} YOUR CHOICE >>>{choice[user_input]}  You WON...")
        User_won+=1
    elif com_choice >user_input:
        print(f"COMPUTER CHOICE >>>\n{choice[com_choice]} YOUR CHOICE >>>{choice[user_input]} You LOST...")
        computer_won+=1    
    else:
        print("invalid input....")    
    i+=1
if computer_won>User_won:
    print("Computer Won The CHAMPIONSHIP....")
elif computer_won<User_won:
    print("You Won The CHAMPIONSHIP....")
else:
    print("Its a DRAW.. ")    

