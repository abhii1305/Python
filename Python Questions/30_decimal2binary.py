def conv_binary(n):
    if n>1:
        conv_binary(n//2)

    print(n%2,end="")
num = int(input("Enter the number:"))
print("The binary of the number is:")
conv_binary(num)