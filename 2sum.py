arr=[2,5,3,1,8,4]
target=7
arr.sort()
def twosum(arr,target):
    l=0
    e=len(arr)-1
    while l<e:
        j=arr[l]+arr[e]
        if j==target:
            return[arr[l],arr[e]]
        elif j<target:
             l+=1
        else:
            e-=1
print(twosum(arr,target))