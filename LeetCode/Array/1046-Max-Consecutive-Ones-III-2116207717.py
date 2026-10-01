class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l,r=0,0
        zeros,maxl=0,0
        while r<n:
            if nums[r]==0:
                zeros+=1
            if zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            if zeros<=k:
                length=r-l+1
                maxl=max(maxl,length)
            r+=1
        return maxl
        