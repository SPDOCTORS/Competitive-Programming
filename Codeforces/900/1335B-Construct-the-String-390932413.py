t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    s=[]
    for i in range(n):
        letterindex=i%b
        letter=chr(ord('a')+letterindex)
        s.append(letter)
    print(''.join(s))