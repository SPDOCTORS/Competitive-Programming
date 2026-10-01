class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total=0
        n=len(nums)
        for num in nums:
            total^=num
        if total!=0:
            return n
        for i in range(n):
            if nums[i]!=0:
                return n-1
        return 0
        