t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    mem=[]
    doc=set()
    for i in range(n):
        if s[i]=="1":
            mem.append(i+1)
        elif s[i]=="2":
            if mem:
                x=mem.pop()
                doc.add(x)
            else:
                doc.add(i+1)
        else:
            doc.add(i+1)
    not_printed=[]
    for j in range(1,n+1):
        if j not in doc:
            not_printed.append(j)
    print(len(not_printed))
    print(*not_printed)