print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    result = num1 + num2
    op = "+"

elif choice == "2":
    result = num1 - num2
    op = "-"

elif choice == "3":
    result = num1 * num2
    op = "*"

elif choice == "4":
    if num2 == 0:
        print("Cannot divide by zero")
        exit()
    result = num1 / num2
    op = "/"

else:
    print("Invalid choice")
    exit()

if result == int(result):
    result = int(result)
if num1 == int(num1):
    num1 = int(num1)
if num2 == int(num2):
    num2 = int(num2)

print(num1, op, num2, "=", result)