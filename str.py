"""CHECK IF STRING SPLIT IN 2 PARTS BOTH STRING HAVE EQUAL NO OF 0 AND 1"""
strq=input()
couone=0
couzer=0
if len(strq)%2!=0:
    print("-1")
    exit()
for i in strq[:len(strq)//2]:
    if i=='0':
        couzer+=1
    else:
        couone+=1
for i in strq[len(strq)//2:]:
    if i=='0':
        couzer-=1
    else:
        couone-=1

if couone == 0 and couzer == 0:
    print(strq[:len(strq)//2])
    print(strq[len(strq)//2:])
else:
    print("-1")
