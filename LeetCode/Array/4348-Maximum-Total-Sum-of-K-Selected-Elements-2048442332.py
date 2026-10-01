class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)
        total=0
        for i in range(k):
            total+=max(nums[i],nums[i]*mul)
            mul-=1
        return total
        