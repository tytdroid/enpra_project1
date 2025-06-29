import random

answer = []
while len(answer) < 3:
    x = random.randint(1, 9)
    if x not in answer:
        answer.append(x)

your_answer = input("Enter your 3-digit guess：")

hit = sum([int(your_answer[i]) == answer[i] for i in range(3)])
blow = sum([int(g) in answer for g in your_answer]) - hit
print(f"{hit} Hit, {blow} Blow")

print(answer,your_answer)      