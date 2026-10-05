t=int(input())
for _ in range(t):
    s=input()
    lower=[]
    upper=[]
    for i in range(len(s)):
        if s[i]=='b':
            if lower:
                lower.pop()
        elif s[i]=='B':
            if upper:
                upper.pop()
        elif s[i].islower():
            lower.append(i)
        else:
            upper.append(i)
    remaining=lower+upper
    remaining.sort()
    ans=''.join(s[i] for i in remaining)
    print(ans)