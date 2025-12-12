def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b
while True:
    print("\n=== Calculator Menu ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = int(input("Enter your choice (1-5): "))
    if choice == 5:
        print("Calculator Closed.")
        break
    if choice in [1, 2, 3, 4]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == 1:
            print("Result:", add(num1, num2))
        elif choice == 2:
            print("Result:", sub(num1, num2))
        elif choice == 3:
            print("Result:", mul(num1, num2))
        elif choice == 4:
            print("Result:", div(num1, num2))
    else:
        print("Invalid choice! Try again.")
