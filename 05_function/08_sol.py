# Create a function that accepts any number of keyword argumenmts and prints them in the fromat KEY:value.
def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:,{value}")


print_kwargs(name="Shaktiman",power="lazer")
print_kwargs(name="shaktiman",power="helicopter")
