# sort a dictionary by value

marks = {"abhi":27,"aman":25,"rahul":10,"jeet":30}

sorted_value = sorted(marks.items() ,key = lambda x : x[1])
print(sorted_value)

# sort ony thr values

value = sorted(marks.values())
print(value)