num = int(input("Enter a number:"))
if num ==1:
    print (num," is not a prime number")
if num>1:

    for i in range (2,num):
      if num % i ==0:
        print(num," is not a prime number")
        break
    else:
        print(num," is a prime number")



# n= int(input("Enter any number: "))
# if (n%n==0) and (n%2!=0) and (n>1):
#     print("Given number is a prime ")
# else:
#     print("No is not a prime ")
        