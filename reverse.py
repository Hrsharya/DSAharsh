arr=[2,3,4,6,7]
def reverse(arr):
    st=0
    end=len(arr)-1
    while st<=end:
        arr[st],arr[end]=arr[end],arr[st]
        st+=1
        end-=1
reverse(arr)
print(arr)