fruit = input('Enter your fruit : ')

if fruit == 'banana':
    color = input('Enter the color of your fruit : ')
    if color == 'green':
     print("You're fruit is unripe..")
    elif color == 'yellow':
        print("You're fruit is perfectly ripe")
    elif color == 'brown':
     print("You're fruit is overripe..")
    else : 
        print("Enter the correct color..!")
else :
   print("You're fruit is not banana")

