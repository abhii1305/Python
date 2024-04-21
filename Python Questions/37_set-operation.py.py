
# perform different SET operations like--  Union, Intersection, Difference, Symmetric Difference


# union-- |
# Intersection -- &
# Diff.-- -
# symm.diff. --^


a = {1,2,3,4,5,6}
b={3,4,5,6,7,8,9}

print("The union of a and b is:", a | b)
print("The intersection of a and b is:", a & b)
print("The difference of a and b is:", a - b)
print("The symm. diff. of a and b is:", a ^ b)