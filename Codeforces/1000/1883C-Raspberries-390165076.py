t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans=float('inf')
    cnt_even=0
    for i in range(n):
        ops=(k-(a[i]%k))%k
        ans=min(ans,ops)
        if a[i]%2==0:
            cnt_even+=1
        if k==4:
            y=max(0,2-cnt_even)
            ans=min(ans,y)
    print(ans)