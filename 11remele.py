arr=[1,2,3,4,5,5,5,6,7,7,8,9,9,10]
k=6
for i in arr:
    if i==k:
        arr.remove(i)
print(arr)