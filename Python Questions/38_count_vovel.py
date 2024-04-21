#  count the  number of each vovel in a given string
# casefold() is used to change the alphabets into small case

# using dictionary

a = "Ms Dhoni is the Greatest Finisher and Captain of all time"
vovels = "aeiou"
a= a.casefold()
print(a)
count = {}.fromkeys(vovels,0)

for char in a:
    if char in count:
        count[char]+= 1


print(count)