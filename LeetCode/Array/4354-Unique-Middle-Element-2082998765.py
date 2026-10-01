class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        left=0
        right=len(nums)-1
        mid=nums[len(nums)//2]
        while left<right:
            if nums[left]==mid or nums[right]==mid:
                return False
            left+=1
            right-=1
        return True