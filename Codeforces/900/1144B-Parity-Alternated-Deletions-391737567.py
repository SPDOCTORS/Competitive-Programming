n=int(input())
a=list(map(int,input().split()))
a.sort()
odd=[]
even=[]
for x in a:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
if len(odd)>len(even):
    larger=odd
    L=len(odd)
    k=len(even)
else:
    larger=even
    L=len(even)
    k=len(odd)
remaining=L-(k+1)
if remaining<=0:
    print(0)
else:
    print(sum(larger[:remaining]))