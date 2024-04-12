def natural_num_sum(n):
    if n<=1:
        return n
    else:
        return(n)+natural_num_sum(n-1)
    
n=int(input("enter a number:"))

if n<=0:
    print("Enter a positive  number")

else:
    print("The sum of natural number upto given number is:",natural_num_sum(n))

