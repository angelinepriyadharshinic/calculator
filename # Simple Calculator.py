# Simple Calculator

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponent")

choice = input("Enter your choice (1-5): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = num1 + num2
    print("Result:", result)

elif choice == '2':
    result = num1 - num2
    print("Result:", result)

elif choice == '3':
    result = num1 * num2
    print("Result:", result)

elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")

elif choice == '5':
    result = num1 ** num2
    print("Result:", result)

else:
    print("Invalid choice. Please select a number between 1 and 5.")