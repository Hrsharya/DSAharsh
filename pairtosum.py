arr=[1,2,3,4,5,6,7,8,9,10]
k=8
def pairtosum(arr,k):
    for i in range (len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==k:
                print(arr[i],arr[j])
print(pairtosum(arr,k))