x = 300
print("Find the closest number to", x)

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))

diff_a = abs(x - a)
diff_b = abs(x - b)
diff_c = abs(x - c) 

min_diff = min(diff_a, diff_b, diff_c)

if diff_a == diff_b == diff_c:
    print("All numbers are equally closest to", x)

elif diff_a == min_diff and diff_b == min_diff:
    print("A and B are the closest numbers to", x)

elif diff_a == min_diff and diff_c == min_diff:
    print("A and C are the closest numbers to", x)

elif diff_b == min_diff and diff_c == min_diff:
    print("B and C are the closest numbers to", x)

elif diff_a == min_diff:
    print("A or", a, "is the closest number to", x)

elif diff_b == min_diff:
    print("B or", b, "is the closest number to", x)

else:
    print("C or", c, "is the closest number to", x)