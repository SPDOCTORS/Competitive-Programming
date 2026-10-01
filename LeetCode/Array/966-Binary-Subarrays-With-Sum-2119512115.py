class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(goal):
            if goal<0:
                return 0
            l,r=0,0
            sum_val=0
            count=0
            while r<len(nums):
                sum_val+=nums[r]
                while sum_val>goal:
                    sum_val-=nums[l]
                    l+=1
                count+=(r-l+1)
                r+=1
            return count
        return atmost(goal)-atmost(goal-1)
        