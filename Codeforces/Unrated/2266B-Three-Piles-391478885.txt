t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    ans=max(abs(a-b),abs(a+c-b))
    print(ans)