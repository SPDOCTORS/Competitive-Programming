t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ok=True
    for level in range(1,n+1):
        left=0
        right=n
        while left<right:
            mid=(left+right)//2
            if a[mid]>=level:
                left=mid+1
            else:
                right=mid
        count=left
        if a[level-1]!=count:
            ok=False
            break
    if ok:
        print("YES")
    else:
        print("NO")