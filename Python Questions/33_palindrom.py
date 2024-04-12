a= input("Enter a word here: ")

rev = a[:: -1]

if a == rev:
    print("it is palindrom")
else:
    print("It is not a palindrome")