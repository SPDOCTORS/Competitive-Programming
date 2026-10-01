import math
class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n=len(nums)
        midi=nums[n//2]
        cnt=0
        for num in nums:
            if num==midi:
                cnt+=1
            if cnt>1:
                return False
        return True

        