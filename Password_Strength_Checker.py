# taking password as input from user
password = input("Enter password")
upper = 0
lower = 0
digit = 0
spl = 0

# ensuring password is more than 8 characters
while (True):
    if (len(password) < 8):
        print("Password is too short")
        password = input("Enter password")
    else:
        break

# checking the characters
for chr in password:
    if (chr.isupper()):
        upper += 1
    elif (chr.islower()):
        lower += 1
    elif (chr.isdigit()):
        digit += 1
    else:
        spl += 1

# deciding if the password is Strong, Intermediate or Weak
if (len(password) >= 8 and upper >= 1 and lower >= 1 and digit >= 1 and spl >= 1):
    print("Password is Weak")

elif (len(password) >= 8 and (upper + digit + spl >= 3)):
    print("Password is Intermediate")

else:
    print("Password is Strong")