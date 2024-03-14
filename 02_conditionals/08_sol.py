# password checker

password = input("Enter password")

if len(password) < 6:
    strenght = "weak"
elif len(password) < 10:
    strenght = "meduim"
else:
    strenght = "strong"

    print("Password strenght is:", strenght)