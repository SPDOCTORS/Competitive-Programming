t=int(input())
for _ in range(t):
    x,n=map(int,input().split())
    r=n%4
    if r==0:
        change=0
    elif r==1:
        change=-n
    elif r==2:
        change=1
    else:
        change=n+1
    if x%2==0:
        print(x+change)
    else:
        print(x-change)