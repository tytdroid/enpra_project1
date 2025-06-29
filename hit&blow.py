import random

limit=10#回数制限
answer = []#答えの設定

while len(answer) < 3:
    x = random.randint(1, 9)
    if x not in answer:
        answer.append(x)

for i in range(limit):
    your_answer = input("Enter your 3-digit guess：")#回答の入力

    hit = sum([int(your_answer[i]) == answer[i] for i in range(3)])#結果＆ヒント
    blow = sum([int(g) in answer for g in your_answer]) - hit
    print(f"{hit} Hit, {blow} Blow")

    if your_answer == ''.join(map(str, answer)):
        print("Correct!")
        break
else:
    print(f"You failed! The answer was {''.join(map(str, answer))}")  