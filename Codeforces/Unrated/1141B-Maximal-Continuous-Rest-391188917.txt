n=int(input())
a=list(map(int,input().split()))
prefix=0
for i in range(n):
    if a[i]==1:
        prefix+=1
    else:
        break
suffix=0
for i in range(n-1,-1,-1):
    if a[i]==1:
        suffix+=1
    else:
        break
count=0
maxi=0
for i in range(n):
    if a[i]==1:
        count+=1
        maxi=max(maxi,count)
    else:
        count=0
ans=max(maxi,prefix+suffix)
print(ans)