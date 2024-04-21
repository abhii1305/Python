a = "Ms Dhoni is the Greatest Finisher and Captain of all time"

w = a.split ()
# print(w)

for i in range(len(w)):
    w[i] = w[i].lower()




w.sort()
print(w)

for i in w:
    print(i)