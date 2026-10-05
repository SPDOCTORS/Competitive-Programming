t=int(input())
for _ in range(t):
    n=int(input())
    a1,a2,a3=map(int,input().split())
    ans=n-min(a1,a2,a3)
    print(ans)