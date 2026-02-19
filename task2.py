print("Enter and compare two numbers")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("First number: ", num1,)
print("Second number: " , num2)

if (num1 > num2):
    print("First number (", num1, ") is greater than second number (", num2, ")")
elif (num1 < num2):
    print("Second number (", num2, ") is greater than First number (", num1, ")")
else:
    print("First number (", num1, ") and second number (", num2, ") are equal")