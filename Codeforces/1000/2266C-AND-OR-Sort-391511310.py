t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    if s[0]=="1":
        print(s.count("0"))
        continue
    right_zero=s.count("0")
    left_one=0
    mini=float("inf")
    for ch in s:
        if ch=="0":
            right_zero-=1
        else:
            left_one+=1
        operations=right_zero+left_one
        mini=min(mini,operations)
    print(mini)