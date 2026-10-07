t=int(input())
for _ in range(t):
    x0,y0,R=map(int,input().split())
    x=x0-R
    y=y0
    print(x,y)