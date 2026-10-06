# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    window=n-k
    sumi=0
    for i in range(window):
        sumi+=A[i]
    maxi=sumi
    for i in range(window,n):
        sumi=sumi-A[i-window]+A[i]
        maxi=max(maxi,sumi)
    print(maxi)
    
