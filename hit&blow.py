import random

answer = []
while len(answer) < 3:
    x = random.randint(1, 9)
    if x not in answer:
        answer.append(x)

your_answer = input("Enter your 3-digit guess：")

print(answer,your_answer)      