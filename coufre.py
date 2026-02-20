arr=[1,1,1,2,2,3,3,3,4,4]
def coufre(arr):
    sej={}
    for i in arr:
        if i in sej:
            sej[i]+=1
        else:
            sej[i]=1
    return sej
print(coufre(arr))
