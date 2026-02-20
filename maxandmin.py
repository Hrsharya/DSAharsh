arr=[1,2,3,4,7,2,1]
def maxmin(arr):
    max=arr[0]
    min=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max:
            max=arr[i]
        elif arr[i]<min:
            min=arr[i]
    return max,min
print(maxmin(arr))