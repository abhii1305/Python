num = int(input("enter the number:"))
order = len(str(num))
sum = 0
temp = num


while temp >0:
    
   digit = temp %10
   cube = digit ** order
   sum = sum + cube
   temp //= 10

if sum == num:
   print(num,"is a armstrong number")

else:
   print(num,"is not a armstrong number")