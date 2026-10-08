t=int(input())
for _ in range(t):
    x=int(input())
    if x>45:
        print(-1)
        continue
    digits=[]
    while x>0:
        for i in range(9,0,-1):
            if x>=i:
                digits.append(i)
                x-=i
        digits.sort()
        ans=''.join(str(i) for i in digits)
    print(ans)