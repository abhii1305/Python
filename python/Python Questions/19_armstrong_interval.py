lower = int(input("Enter the lower limit:"))
upper = int(input("Enter the upper limit:"))

for num in range (lower,upper+1):
  order = len(str(num))
  sum = 0
  temp = num

  while temp > 0:
    digit = temp%10
    cube = digit ** order
    sum = sum + cube
    temp //= 10


  if sum == num:
    print(sum)
