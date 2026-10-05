n=int(input())
a=list(map(int,input().split()))
case1 = a.copy()
case2 = a.copy()
case1.remove(max(case1))
case2.remove(min(case2))
maxi=max(case1)
mini=min(case1)
final=maxi-mini
maxi_1=max(case2)
mini_1=min(case2)
final1=maxi_1-mini_1
ans=min(final,final1)
print(ans)