arr=[1,2,3,5,4,6,7,8,9,10]
def chec(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
        else:
            True
print(chec(arr))