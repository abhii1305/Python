# MULTIPLICATION WITH SKIP 5TH ITTERATION
n=int(input("Enter the number:"))

for i in range(1,11):
    if i ==5:
        continue


    print(n, 'x',i, '=', n*i)
