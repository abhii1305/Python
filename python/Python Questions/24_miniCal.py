print("~~~~~~~MIni Calculator~~~~~~~~~``")

num1 = float(input("enter the first number:"))
num2= float(input("enter the second number"))

print("press 1 for addition \npress 2 for substraction \npress 3 for multiplication \npress 4 for division")

choice  = int(input("Enter your choice from 1 to 4:"))

if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(num1-num2)
elif choice == 3:
    print(num1*num2)
elif choice == 4:
    print(num1%num2)
else:
    print("invalid choice!")


# num1=int(input("First number:"))
# num2=int(input("Second number:"))
# opr=input("Enter the operator(+, -, *, /)")
# if opr =="+":
# 	print(num1+num2)
# if opr =="-":
# 	print(num1-num2)
# if opr =="*":
# 	print(num1*num2)
# if opr =="/":
# 	print(num1/num2)
# if opr!='+' and opr!='-' and opr!='*' and opr!='/':
# 	print('Invalid Input!')