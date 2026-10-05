class Solution:
    def minRotations(self, n: int, s: str) -> int:
        n=len(s)
        total=0
        distance=abs(0-int(s[0]))
        circular=10-distance
        total+=min(distance,circular)
        for i in range(n-1):
            distance=abs(int(s[i])-int(s[i+1]))
            circular=10-distance
            total+=min(distance,circular)
        mini=total
        distance=abs(0-int(s[0]))
        circular=10-distance
        old_bound=min(distance,circular)
        distance=abs(0-int(s[n-1]))
        circular=10-distance
        new_bound=min(distance,circular)
        new=total-old_bound+new_bound
        mini=min(mini,new)
        for k in range(1,n):
            distance=abs(int(s[k-1])-int(s[k]))
            circular=10-distance
            old_bound=min(distance,circular)
            distance=abs(int(s[k-1])-int(s[n-1]))
            circular=10-distance
            new_bound=min(distance,circular)
            newi=total-old_bound+new_bound
            mini=min(mini,newi)
        return mini
        