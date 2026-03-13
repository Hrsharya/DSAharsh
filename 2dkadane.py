import sys
matrix=[[1,2,3,4],[5,6,7,8],[9,8,7,6],[5,4,3,2]]
def kadanealgo(arrz):
    st,end,currsum=0,0,0
    maxsum=-sys.maxsize
    while end<len(arrz):
        while currsum<0:
            currsum-=arrz[st]
            st+=1
        currsum+=arrz[end]
        end+=1
        maxsum=max(maxsum,currsum)
    return maxsum

n=len(matrix)
m=len(matrix[0])
ans=-sys.maxsize
for i in range(m):
    tem=[]
    for j in range(n):
        tem.append(matrix[j][i])
        print(tem)
    ans=(max(ans,kadanealgo(tem)))
    for j in range(i+1,m):
        for k in range(n):
            tem[k]+=matrix[k][j]
        print(tem)
        ans=(max(ans,kadanealgo(tem)))
print(ans)