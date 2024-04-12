num = int(input("enter a number:"))
# print(sum(range(1,num+1)))

if num <0:
    print("Enter positive number")

else:
    sum = 0
    while num>0:
        sum = sum+num
        num = num-1


print(sum)
