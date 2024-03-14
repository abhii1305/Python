# PET FOOD RECOMMENDATION
pet=input("choose your pet species:\n")



age =int(input("write age of your species:\n"))

if pet =="dog" and age <=2:
    print("give puppy food")
elif pet =="dog" and age >=2:
    print("give dog food")

elif pet =="cat" and age >=5:
    print("give senior cat food")
elif pet =="cat" and age <=5:
    print("give pussy food")
    
else:
    print("i dont have any other data")
   
    