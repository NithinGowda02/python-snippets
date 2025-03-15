import random

def roll():
    min_Value = 1
    max_value = 6
    roll = random.randint(min_Value,max_value)
    return roll
while True:
    players = input("Enter the number of players (2-4) >> ")
    if players.isdigit():
        players = int(players)
        if players >= 2 and players <= 4:
            break
        else:
            print("Invalid Input Try Again with (2-4)")
    else:
        print("Inavlid Input..!") 

max_score = 50
Player_Score = [0 for _ in range(players)] 

while max(Player_Score) < max_score:
    for player_idx in range(players):
        print(f"\nPlayer number-{player_idx+1} turn has just Started..\n")
        print(f"Your total score is >> {Player_Score[player_idx]}\n")
        current_Score = 0

        while True:
            turn = input("Would you like roll (y)? >> ")
            if turn.lower() != 'y':
                break
            value = roll()
        
            if value == 1:
                print("You Rolled a 1..! Your Turn Done")
                current_Score = 0
                break
            else:
                current_Score += value
                print(f"You Rolled a >>  {value}")

            print(f"Your Score >>  {current_Score}")

        Player_Score[player_idx]  += current_Score
        print(f"Your Total Score is >> {Player_Score[player_idx]}")
maxi_score = max(Player_Score)
winning_Idx = Player_Score.index(maxi_score)          
print(f"Player Number-{winning_Idx+1} is the winner with max score of >> {maxi_score}")




