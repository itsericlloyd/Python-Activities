def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return "num1", num1
    elif num2 >= num1 and num2 >= num3:
        return "num2", num2
    else:
        return "num3", num3


# Get input from user
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

letter, largest = find_largest(num1, num2, num3)

print(f" {letter} is the largest number with a value of {largest}")