# using for loop

# num = int(input("enter a number:"))

# fact = 1

# if num<0:
#     print("factorial of 0 doesn't exists")
# if num ==0:
#     print("factorial of 0 is",1)
    
# if num>0:
#     for i in range (1,num+1):
#         fact =fact * i

# print("the factorial of the given number is", fact)



# using recursiuon

def fact(a):

    f=1
    for i in range(1,a+1):
        f=f*i

    return f

a = int(input("eneter a number:"))
factorial = fact(a)
print("the factorial of the given number is",factorial)