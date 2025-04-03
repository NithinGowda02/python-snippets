print("WELCOME TO MY QUIZ GAME...")
print("===========================")
play = input("Do you want to play >> ").lower()
if play != "yes":
    quit()

print("Let's start the Game :)") 
print("===========================")

print("You need to answer 5 questions".upper())
score = 0
question = input("What does CPU stands for? >> ").lower()
if question == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorect!")   

question = input("What does RAM stands for? >> ").lower()
if question == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorect!")

question = input("What does ROM stands for? >> ").lower()
if question == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorect!")   

question = input("What is the Capital of India? >> ").lower()
if question == "delhi":
    print("Correct!")
    score += 1
else:
    print("Incorect!")

question = input("who is the first cricketer to score 200 in ODI Cricket >> ").lower()
if question == "sachin tendulkar":
    print("Correct!")
    score += 1
else:
    print("Incorect!") 
print("***************************************")
print(f"Your score >> {score}") 
 
print(f"Thank you for Playing. you got {(score/5) *100}%.")
print("***************************************")               