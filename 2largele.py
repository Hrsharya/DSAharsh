arr=[1,3,4,5,6,7,8,6,9]
m=0
def second_largest(arr):
  j=max(arr)
  arr.remove(j)
  print(max(arr))
second_largest(arr)
"""  if len(arr)<2:
        return None
    m=arr[0]
    sm=None
    for i in range(1,len(arr)):
        if arr[i]>m:
            sm=max(sm,m) if sm is not None else m
            m=arr[i]
        elif arr[i]>sm and arr[i]!=m:
            sm=arr[i]
    return sm
print(second_largest(arr))"""
    
