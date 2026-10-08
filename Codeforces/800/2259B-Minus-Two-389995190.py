t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    odd=0
    div4=0
    even_but_not_div4=0
    for i in range(n):
        if a[i]%2==1:
            odd+=1
        elif a[i]%4==0:
            div4+=1
        else:
            even_but_not_div4+=1
    print(max(odd,div4,even_but_not_div4))