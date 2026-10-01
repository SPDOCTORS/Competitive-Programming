class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums=[x for x in nums if lower<=x<=upper]
        nums.sort()
        if not nums:
            return [[lower,upper]]
        n=len(nums)
        ans=[]
        if nums[0]>lower:
            ans.append([lower,nums[0]-1])
        for i in range(0,n-1):
            if nums[i+1]>nums[i]+1:
                ans.append([nums[i]+1,nums[i+1]-1])
        if nums[-1]<upper:
            ans.append([nums[-1]+1,upper])
        return ans

        