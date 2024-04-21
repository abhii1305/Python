# enumerate() will automatically keep track of the order in which items are accessed, which gives us the index value without the need to maintain a separate index variable.

l = [23,4,55,65]
for index , value in enumerate(l,start=1,):
    print(index,"-" ,  value)

#     # without using thr enumerate method
# l = [23,4,55,65]
# for index in range(len(l)):
#     value = l[index]
#     print(index,value) 