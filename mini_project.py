password = str(input("Enter your password: "))
password_len = len(password)

for char in password:
    if char.isdigit():
        num = True
    else:
        num = False

if (password_len >= 8 and num == True):
    print("Password accepted")
elif (password_len < 8 and num == False):
    print("Requirements not met")
    print("Password must be atleast 8+ characters long and contain 1 number")
elif (password_len < 8 and num == True):
    print("Requirements not met")
    print("Password must be atleast 8+ characters long")
elif (password_len >= 8 and num == False):
    print("Requirements not met")
    print("Password must contain atleast 1 number")