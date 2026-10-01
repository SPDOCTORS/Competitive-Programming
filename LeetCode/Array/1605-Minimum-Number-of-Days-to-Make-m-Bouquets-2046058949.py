class Solution:
    def poss(self,bloomDay,days,m,k):
        n=len(bloomDay)
        cnt=0
        bo=0
        for i in range(n):
            if bloomDay[i]<=days:
                cnt+=1
            else:
                bo+=(cnt//k)
                cnt=0
        bo+=(cnt//k)
        return bo>=m
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        val=m*k
        n=len(bloomDay)
        if val>n:
            return -1
        maxi=float('-inf')
        mini=float('inf')
        for num in bloomDay:
            maxi=max(maxi,num)
            mini=min(mini,num)
        low=mini
        high=maxi
        ans=-1
        while low<=high:
            mid=low+(high-low)//2
            if self.poss(bloomDay,mid,m,k):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

        