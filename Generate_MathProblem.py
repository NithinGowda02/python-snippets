import random
import time

OPERATORS = ["+","-","*"]
START_NUM = 2
END_NUM = 20
TOTAL_PROBLEMS = 10

def generate_problem():
    operand_left = random.randint(START_NUM,END_NUM)
    operand_right = random.randint(START_NUM,END_NUM)
    operator = random.choice(OPERATORS)
    expression = str(operand_left) +" "+operator +" "+str(operand_right)
    final_answer = eval(expression)
    return expression, final_answer  
wrong = 0
input("Press enter to start..")
print("-----------------------------")
start_time = time.time()
for i in range (TOTAL_PROBLEMS):
    expression, final_answer = generate_problem()
    while True:
        guess = input(f"Problem #{i+1} : {expression} = ") 
        if guess == str(final_answer):
            break 
        wrong +=1
end_time = time.time()
total_time = round(end_time - start_time,2)
print("------------------------------------------------------------------")
print(f"Total time taken to complete the Problems {total_time} seconds.")
print("------------------------------------------------------------------")        

