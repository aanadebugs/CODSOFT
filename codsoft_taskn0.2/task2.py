def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Error: Division by zero is not allowed"


def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

   
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    choice = input("Enter your operation choice (1/2/3/4): ")

   
    if choice == '1':
        print(f"{n1} + {n2} = {add(n1, n2)}")
    elif choice == '2':
        print(f"{n1} - {n2} = {subtract(n1, n2)}")
    elif choice == '3':
        print(f"{n1} * {n2} = {multiply(n1, n2)}")
    elif choice == '4':
        print(f"{n1} / {n2} = {divide(n1, n2)}")
    else:
        print("Invalid choice")


calculator()