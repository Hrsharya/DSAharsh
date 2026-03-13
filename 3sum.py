arr=[2,5,3,1,8,4]
temp=arr.copy()
target=7
arr.sort()
def threesum(arr,target):
    for i in range (len(arr)-2):
        l=i+1
        r=len(arr)-1
        while l<r:
            s=arr[i]+arr[l]+arr[r]
            if s==target:
                ans=[]
                for j in temp:
                    if j==arr[i] or j==arr[l] or j==arr[r]:
                        ans.append(temp.index(j))
                return[arr[i],arr[l],arr[r],ans]
            if s<target:
                l+=1    
            else:                r-=1
print(threesum(arr,target))
