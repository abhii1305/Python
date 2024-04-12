# using for loop

# print("The number divisible by 13 are:")
# for i in range (1,100):
#     if i % 13 ==0:
#         print(i)


        # using lambda function and filter()

l = [39,44,55,664,64,6556,556,52]
result = list(filter(lambda x : x%13==0,l))

print("the number divisible by 13 are:",result)