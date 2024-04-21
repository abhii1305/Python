# using '+' operator

l1 = [1,3,4,"a","b"]
l2 = [2,4,5,"f","b"]
conc = (l1+l2)
print(conc)

# using extend()

l1 = [1,3,4,"a","b"]
l2 = [2,4,5,"f","b"]

l1.extend(l2)
print(l1)


# add with unique value
# using set

l1 = [1,3,4,"a","b"]
l2 = [2,4,5,"f","b"]
conc = list(set(l1+l2))
print(conc)
