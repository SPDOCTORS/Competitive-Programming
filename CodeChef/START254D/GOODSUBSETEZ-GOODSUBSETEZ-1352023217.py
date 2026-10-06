# cook your dish here
t=int(input())
for _ in range(t):
    N=int(input())
    S=list(map(int,input().split()))
    count=[0]*31
    for x in S:
        count[x.bit_length()]+=1 
        
    answer=max(count)
    print(answer)