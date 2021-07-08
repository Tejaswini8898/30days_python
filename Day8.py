n = int(input("Enter the starting num:  "))
m = int(input("Enter the ending num: "))
sum = 0
for i in range(n, m+1):
    if (i%2 == 0):
        sum = sum + i
print(sum)
