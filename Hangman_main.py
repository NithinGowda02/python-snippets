hangman=["""
    +---+
    |   |
    O   |
  / | \ |
   / \  |
        |          
""","""
   +---+
    |   |
    O   |
  / | \ |
   /    |
        |
""","""
   +---+
    |   |
    O   |
  / | \ |
        |
        |
""","""
   +---+
    |   |
    O   |
  / |   |
        |
        |
""","""
   +---+
    |   |
    O   |
  /     |
        |
        |
""","""
   +---+
    |   |
    O   |
        |
        |
        |
""","""
   +---+
    |   |
        |
        |
        |
        |
"""
         ]
words=["apple"
       "banana",
      "pineapple",
      "orange",
       "grapes",
       "watermelon"]
import random
guess=random.choice(words)
display=[]
for i in range(len(guess)):
    display+="_"
print(display)

game_over=False
live=6
while not game_over:
    user_guess=input("Enter your letter (Based on fruit name..)>> ").lower()
    for position in range(len(guess)):
        r_letter=guess[position]
        if r_letter==user_guess:
            display[position]=user_guess
    print(display)            
    if user_guess not in guess:
        live-=1
        if live==0:
            game_over=True
            print("You Lose...!")
    if '_' not in display:
        game_over=True
        print("You Won...!") 
    print(hangman[live])                 