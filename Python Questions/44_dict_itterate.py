a = {1:'abhi',2:'mayank',3:"aman"}
# print(a)
# print(a[2])

# with .item()

for key,value in a.items():
    print(key,"-",value)

# # with keys

# for key in a:
#     print(key,"-", a[key])


# with keys and value

for key in  a.keys():
    print(key)     #for printing only key 
    
for i in  a.values():
    print(i)
