# cook your dish here
A,B=map(int,input().split())
if (A-B)%2==0:
    x=(A-B)//2
    print(x)
else:
    print(-1)