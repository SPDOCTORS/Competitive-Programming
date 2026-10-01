class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        mpp={}
        for i in range(n):
            mpp[nums[i]]=mpp.get(nums[i],0)+1
        if k==len(nums):
            return max(nums)
        if k==1:
            maxval= -1
            for i in range(n):
                if mpp[nums[i]]==1 and nums[i]>maxval:
                    maxval=nums[i]
            return maxval
        n=n-1
        if nums[0]==nums[n]:
            return -1
        if mpp[nums[0]]==1 and mpp[nums[n]]==1:
            return max(nums[0],nums[n])
        if mpp[nums[0]]==1 and mpp[nums[n]]>1:
            return nums[0]
        if mpp[nums[0]]>1 and mpp[nums[n]]==1:
            return nums[n]
        return -1       