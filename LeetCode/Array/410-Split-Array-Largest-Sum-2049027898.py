class Solution:
    def count(self,nums,maxsum):
        n=len(nums)
        partition=1
        sub=0
        for i in range(n):
            if sub+nums[i]<=maxsum:
                sub+=nums[i]
            else:
                partition+=1
                sub=nums[i]
        return partition
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=low+(high-low)//2
            if self.count(nums,mid)<=k:
                high=mid-1
            else:
                low=mid+1
        return low
        