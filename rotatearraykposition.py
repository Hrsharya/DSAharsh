arr=[1,2,3,4,5,6,7,8,9,10]
k=3
def rotate(arr,k):
    return arr[k-1:]+arr[:k-1]
print(rotate(arr,k))    