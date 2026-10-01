class Solution:
    def findMax(self,piles):
        n=len(piles)
        maxi=float('-inf')
        for i in range(n):
            maxi=max(maxi,piles[i])
        return maxi
    def totalH(self,piles,hourss):
        totalH=0
        n=len(piles)
        for i in range(n):
            totalH+=math.ceil(piles[i]/hourss)
        return totalH
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high=1,self.findMax(piles)
        while low<=high:
            mid=low+(high-low)//2
            totalH=self.totalH(piles,mid)
            if totalH<=h:
                high=mid-1
            else:
                low=mid+1
        return low
        