t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    mx=max(a)
    ans=-1
    for i in range(n):
        if a[i]==mx:
            if i>0 and a[i-1]<mx:
                ans=i+1
                break
            if i<n-1 and a[i+1]<mx:
                ans=i+1
                break
    print(ans)