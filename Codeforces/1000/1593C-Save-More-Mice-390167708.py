t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    x=list(map(int,input().split()))
    x=sorted(x,reverse=True)
    cat_pos=0
    ans=0
    for i in range(k):
        if cat_pos<x[i]:
            cat_pos+=n-x[i]
            ans+=1
        else:
            break
    print(ans)