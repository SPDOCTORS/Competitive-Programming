t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    possible=True
    for i in range(0,n-2):
            x=a[i]
            a[i]-=x
            a[i+1]-=2*x
            a[i+2]-=x
            if a[i]<0 or a[i+1]<0 or a[i+2]<0:
                possible=False
                break
    if possible and a[n-2]==0 and a[n-1]==0:
        print("YES")
    else:
        print("NO")