t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    set_a=set()
    set_b=set()
    for x in a:
        if 1<=x<=k:
            set_a.add(x)
    for x in b:
        if 1<=x<=k:
            set_b.add(x)
    forcedA=0
    forcedB=0
    flexible=0
    missing=False
    for i in range(1,k+1):
        if i not in set_a and i not in set_b:
            missing=True
        if i in set_a and i not in set_b:
            forcedA+=1
        if i in set_b and i not in set_a:
            forcedB+=1
        if i in set_a and set_b:
            flexible+=1
    need=k//2
    A_remain=need-forcedA
    B_remain=need-forcedB
    if missing or forcedA>need or forcedB>need:
        print("NO")
    else:
        print("YES")