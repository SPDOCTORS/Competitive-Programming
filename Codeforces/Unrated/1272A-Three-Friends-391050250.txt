q=int(input())
for _ in range(q):
    a,b,c=map(int,input().split())
    a,b,c=sorted([a,b,c])
    ans=0
    ans=2*(c-a-2)
    if ans <0:
        print(0)
        continue
    print(ans)