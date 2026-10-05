t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input().strip()
    cnt=0
    for i in range(0,n,k):
        farms=s[i:i+k]
        if '0' not in farms:
            cnt+=1
    print(cnt)