# print("Ms dhoni is best",end = ' ')
# print("and he is God")

# HOW TO CHECK A STRING IS VALID KEYWORD POR NOT

import keyword
# print(keyword.kwlist)

words = ["break","abhijeet","three","continue","lambda","global","for","string",'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with',]

for i in range (len(words)):
    if keyword.iskeyword(words[i]):
        print(words[i],"is a keyword in python")
    else:
        print(words[i],"is not a keyword in python")