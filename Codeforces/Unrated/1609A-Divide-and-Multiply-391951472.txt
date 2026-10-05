t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    stripped=[]
    count=0
    for x in a:
        while x%2==0:
            count+=1
            x=x//2
        stripped.append(x)
    larger=max(stripped)
    larger*=2**count
    ans=sum(stripped)-max(stripped)+larger
    print(ans)