class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n=len(nums)
        sum=nums[0]
        for i in range(1,n):
            if nums[i]==nums[i-1]+1:
                sum+=nums[i]
            else:
                break
        x=sum
        while x in nums:
            x=x+1
        return x
        