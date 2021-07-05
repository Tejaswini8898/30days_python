val = int(input("enter a value: "))
for i in range(val):
    for j in range(i+1):
        print("*",end = "")
    print()
count = val*(val+1)//2
print(count)