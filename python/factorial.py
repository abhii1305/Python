n=int(input('Enter the number-'))

def fact(n):

    f = 1
    for i in range(1, n+1):
        f= f*i

    return f
    

a=5
result=fact(a)
print(result)