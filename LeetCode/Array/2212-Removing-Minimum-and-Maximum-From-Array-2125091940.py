class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        minidx=nums.index(min(nums))
        maxidx=nums.index(max(nums))
        left=min(minidx,maxidx)
        right=max(maxidx,minidx)
        return min(right+1,n-left,left+1+n-right)

        