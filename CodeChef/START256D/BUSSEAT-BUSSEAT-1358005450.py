# cook your dish here
t=int(input())
for _ in range(t):
    N,K=map(int,input().split())
    if K<=N:
        print(0)
        continue
    extra=K-N
    answer=extra*2
    print(answer)
