import random

limit = 10  # 最大回答回数

def generate_answer():
    answer = []
    while len(answer) < 3:
        x = random.randint(1, 9)
        if x not in answer:
            answer.append(x)
    return answer

def get_your_answer():
    while True:
        your_answer = input("Enter your 3-digit your_answer (no duplicates): ")
        if your_answer.isdigit() and len(your_answer) == 3 and len(set(your_answer)) == 3:
            return your_answer
        print("Invalid input. Please enter 3 unique digits (1–9).")

def calculate_hit_blow(your_answer, answer):
    hit = sum([int(your_answer[i]) == answer[i] for i in range(3)])
    blow = sum([int(g) in answer for g in your_answer]) - hit
    return hit, blow

def main():
    answer = generate_answer()
    for attempt in range(limit):
        your_answer = get_your_answer()
        hit, blow = calculate_hit_blow(your_answer, answer)
        print(f"{hit} Hit, {blow} Blow")

        if your_answer == ''.join(map(str, answer)):
            print("Correct!")
            break
    else:
        print(f"You failed! The answer was {''.join(map(str, answer))}")

if __name__ == "__main__":
    main()