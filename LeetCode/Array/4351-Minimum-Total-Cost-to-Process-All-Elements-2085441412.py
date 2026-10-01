class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD=10**9+7
        res=k
        ops=0
        ans=0
        for x in nums:
            if res<x:
                need=(x-res+k-1)//k
                ans=(ans+need*(2*ops+need+1)//2)%MOD
                ops+=need
                res+=need*k
            res-=x
        return ans%MOD
        