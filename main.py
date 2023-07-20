import random
import time

Operators = ["+", "-", "*"]
Min_Operand = 1
Max_Operand = 15
Total_Problems = 10

def generate_problem():
    left = random.randint(Min_Operand, Max_Operand)
    right = random.randint(Min_Operand, Max_Operand)
    operator = random.choice(Operators)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer
    

wrong = 0
input("Press Enter to Start!")
print("---------------------")

start_time = time.time()

for i in range(Total_Problems):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time

print("---------------------")
print("Nice work! You Finished in", total_time, "seconds!")
