t=int(input())
for _ in range(t):
    n=int(input())
    count2=0
    count3=0
    ans=0
    while n%2==0:
        count2+=1
        n=n//2
    while n%3==0:
        count3+=1
        n=n//3
    if count2>count3 or n>1:
        print(-1)
    else:
        ans+=abs(count2-count3)+count3
        print(ans)