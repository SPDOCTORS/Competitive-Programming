# cook your dish here
t=int(input())
for _ in range(t):
    N=int(input())
    A=list(map(int,input().split()))
    b=[]
    for i in range(N):
        if i%2==0:
            b.append(A[i])
        else:
            b.append(-A[i])
            
    diff=abs(b[0])
    for i in range(1,N):
        diff+=abs(b[i]-b[i-1])
    diff+=abs(b[N-1])
    print(diff//2)