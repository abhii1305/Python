# #  python iterators with function

# num = [1,2,3,4,5,6,7]

# # for i in (num):
# #     print(i)

# #    USING NEXT()
# # iterate = iter(num)
# # print(iterate.__next__())
# # print(iterate.__next__())
# # print(iterate)

# class Five:
#     def __init__(self):
#         self.num = 1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#       if self.num<=5:
#         value = self.num
#         self.num+=1
#         return value
#       else:
#         raise StopIteration
    
# ff = Five()
# for i in ff:
#     print(i)