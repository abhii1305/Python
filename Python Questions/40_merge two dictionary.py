# # merging two dictionary using bar (|)operator 

# dict1 = {"abhi":10,"jay":20}
# dict2 = {"jay":30,"rahul":50}

# sum = dict1|dict2

# print(sum)

# # merging two dictionary using exponenet  (**)operator
# dict1 = {"abhi":10,"jay":20}
# dict2 = {"jay":30,"rahul":50}
# sum = {**dict1,**dict2}

# print(sum)

# merging two dictionary using copy and update method 

dict1 = {"abhi":10,"jay":20}
dict2 = {"jay":30,"rahul":50}
dict3 = dict2.copy()
dict3.update(dict1)

print(dict3)