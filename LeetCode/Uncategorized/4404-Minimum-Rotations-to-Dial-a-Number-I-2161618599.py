class Solution:
    def minRotations(self, s: str) -> int:
        n=len(s)
        mini=0
        total=0
        distance = abs(0 - int(s[0]))
        circular = 10 - distance
        total += min(distance, circular)
        for i in range(n-1):
            distance=abs(int(s[i])-int(s[i+1]))
            circular=10-distance
            mini=min(distance,circular)
            total+=mini
        return total
        
        