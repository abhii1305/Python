# remove puntuations sign from a given string like ! ~ ? : "" ' , =


punc = '''!@#$%^&*()_+=|{}[]:;"?/.,~`'''

string = input("Enter anything here :")

empty_str = ""

for i in string:
    if i not in punc:
        empty_str += i

print(empty_str)   