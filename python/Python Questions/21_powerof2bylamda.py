nterm = int(input("enter the range:"))
# anonimus function = lamda funtion
# map is uded to itearte upto the range
result = list(map(lambda x : 2**x,range(nterm+1)))
# print(result)

for i in range (nterm+1):
    
    print("the value of 2 raised to the power",i,"is",result[i])