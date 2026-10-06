# cook your dish here
t=int(input())
for _ in range(t):
    N=int(input())
    if N%2==0:
        ans=N+N//2+1
    else:
        ans=N+N//2
    print(ans)
    
