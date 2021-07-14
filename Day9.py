# val = int(input("Enter the number: "))
# last_digit = val % 10
# print(last_digit)

# using functions
def firstdigit(n):
    while n>= 10:
        n = n/10
    return int(n)
def lastdigit(n):
    n = n% 10
    return int(n)
n = 8765
print(firstdigit(n))
print(lastdigit(n))
