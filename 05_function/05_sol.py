# write a Function to greets a user. If no name is provided, it should greet with a default name
def greet(name= "User"):
    return "Hello," + name + "!"

print(greet("Abhijeet"))
print(greet())