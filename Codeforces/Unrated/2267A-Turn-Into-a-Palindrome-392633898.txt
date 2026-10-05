t=int(input())
for _ in range(t):
    n,c=input().split()
    n=int(n)
    s=input()
    coins=0
    for i in range(n//2):
        left=s[i]
        right=s[n-1-i]
        if left==right:
            continue
        elif left==c or right==c:
            coins+=1
        
        else:
            coins+=2
    print(coins)