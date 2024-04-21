# f = open("file.txt","r")
# lines = f.readlines()

# print(lines)
# new_lines = [x.strip() for x in lines]  #strip method
# print(new_lines)
             

            #  BY LIST COMPREHENSION

f = open("file.txt","r")
lines =[line for line in f]

print(lines)

new_lines = [x.strip() for x in lines]
print(new_lines)