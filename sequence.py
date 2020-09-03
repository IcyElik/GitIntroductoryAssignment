n = int(input("Enter the length of the sequence: "))

n1 = 1
n2 = 2
n3 = 3
count = 0

if n <= 0:
    print("Invalid Integer")
elif n == 1:
    print(n1)
else:
    while count < n:
        print(n1)
        nth = n1 + n2 + n3
        n1 = n2
        n2 = n3
        n3 = nth
        count += 1