import math

def get_two_numbers():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    return a, b

def calculate_and_display(a, b):
    results = {}
    results['+'] = a + b
    results['-'] = a - b
    results['*'] = a * b
    results['/'] = a / b if b != 0 else 'Division by zero error'
    return results

def display_and_save(results, a, b):
    print(f"\n[Results] For numbers: {a} and {b}")
    history = []
    for op, val in results.items():
        line = f"{a} {op} {b} = {val}"
        print(line)
        history.append(line)

def main():
    while True:
        a, b = get_two_numbers()
        results = calculate_and_display(a, b)
        display_and_save(results, a, b)

        cont = input("Do you want to continue? (y/n): ").strip().lower()
        if cont != 'y':
            break

if __name__ == "__main__":
    main()
