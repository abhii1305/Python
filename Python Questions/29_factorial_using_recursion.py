def fact(n):
    if n==0:
        return 1
    else:
        return (n*fact(n-1))
    
num = int(input("Enter a number here: "))
if num<0:
    print("not exists")
else:
    print("factorial of number is:",fact(num))