q=int(input())
for _ in range(q):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    small=min(a)
    large=max(a)
    if small+k>=large-k:
        maxi=small+k
        print(maxi)
    else:
        print(-1)