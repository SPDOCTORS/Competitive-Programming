class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s==0:
            return 0
        if s>9*n:
            return -1
        miami=0
        for _ in range(n):
            d=min(9,s)
            miami=miami*10+d
            
            s-=d
        return miami
            
            
            