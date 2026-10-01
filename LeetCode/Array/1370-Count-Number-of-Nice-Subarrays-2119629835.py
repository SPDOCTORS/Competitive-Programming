class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(k):
            if k<0:
                return 0
            l,r=0,0
            count=0
            sum_val=0
            while r<len(nums):
                sum_val+=nums[r]%2
                while sum_val>k:
                    sum_val-=nums[l]%2
                    l+=1
                count+=r-l+1
                r+=1
            return count
        return helper(k)-helper(k-1)

        