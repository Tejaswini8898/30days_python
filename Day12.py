def linear_search(arr, x, n):
    for i in range(0, n):
        if (arr[i]==x):
            return i

    return -1

arr = [1,3,2,6,0,3,5]
x = 2
n = len(arr)

result = linear_search(arr,x,n)
if (result == -1):
    print("element not found in given arr")
else:
    print("element is present at index",result)


    


