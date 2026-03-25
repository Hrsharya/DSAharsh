def computelps(str,lps):
    n=len(str)
    i=1
    lps[0]=0
    temp=0
    while i<n:
        if str[i]==str[temp]:
            temp+=1
            lps[i]=temp
            i+=1
        else:
            if temp!=0:
                temp=lps[temp-1]
            else:
                lps[i-1]
                i+=1
    print(lps)            
def kmp(a,b):
    n=len(a)
    m=len(b)
    lps=[0]*m
    computelps(b,lps)
    i=0
    j=0
    while i<n:
        if a[i]==b[j]:
            i+=1
            j+=1
        if j==m:
            print("j is a substring")
            return
        elif i<n and a[i]!=b[j]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
    print("b is not a substring")

a="aaaaabbbbccccabc"
b="ababab"
kmp(a,b)
print(5//2)


