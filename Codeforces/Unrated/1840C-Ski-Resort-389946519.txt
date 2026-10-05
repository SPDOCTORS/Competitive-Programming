t=int(input())
for _ in range(t):
    n,k,q=map(int,input().split())
    a=list(map(int,input().split()))
    cnt =0
    ans=0
    for temp in a:
        if temp<=q:
            cnt+=1
            if cnt>=k:
                ans+=cnt-k+1
        else:
            cnt=0
    print(ans)