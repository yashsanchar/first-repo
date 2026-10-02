# building a basic calculator

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
except ValueError:
    print("Please enter valid integers.")
    exit()

o = input("Enter the symbol of the operation you want to perform (+,-,*,/): ")

if o == "+":
    print(f"The sum of two numbers is: {a + b}")
elif o == "-":
    print(f"The difference of two numbers is: {a - b}")
elif o == "*":
    print(f"The product of two numbers is: {a * b}")
elif o == "/":
    if b != 0:
        print(f"The quotient of two numbers is: {a / b}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation symbol. Please use +, -, *, or /.")