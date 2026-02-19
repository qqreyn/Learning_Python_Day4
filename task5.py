print("Age checker")
age = int(input("Enter your age: "))

if (age >= 0 and age <= 100):
    if (age >= 0 and age < 18):
        print("You are an child")
    elif (age >= 18 and age < 65):
        print("You are an adult")
    else:
        print("You are an senior")
else:
    print("INVALID AGE")