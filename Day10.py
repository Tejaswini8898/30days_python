num = int(input("Enter the numbers: "))
if num < 0:
    print("Enter positive number")
else:
    sum = 0
    for i in range(0, num+1):
        sum += num
        num -= 1
    print(sum)





    