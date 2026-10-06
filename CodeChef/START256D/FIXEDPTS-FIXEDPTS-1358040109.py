# cook your dish here
t=int(input())
for _ in range(t):
    N,K=map(int,input().split())
    if K==N-1:
        print("No")
    else:
        print("Yes")
    