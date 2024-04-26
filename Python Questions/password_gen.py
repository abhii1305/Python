# Python code to gentrate random password or suggest password

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = "".join(random.choice(characters) for i in range(length))

    return password

length = int(input("Enter password length: "))
password = generate_password(length)
print("Your Password is:",password)