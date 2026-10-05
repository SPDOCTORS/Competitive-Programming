q=int(input())
for _ in range(q):
    n=int(input())
    p=list(map(int,input().split()))
    p=[x-1 for x in p]
    ans=[]
    for i in range(n):
        start=i
        current=i
        days=0
        current=p[current]
        days+=1
        while start!=current:
            current=p[current]
            days+=1
        ans.append(days)
    print(*ans)