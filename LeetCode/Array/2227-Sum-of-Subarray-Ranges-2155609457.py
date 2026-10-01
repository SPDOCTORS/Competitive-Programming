class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        n=len(nums)
        total_sum=0
        for i in range(n):
            smallest=nums[i]
            largest=nums[i]
            for j in range(i,n):
                smallest=min(smallest,nums[j])
                largest=max(largest,nums[j])
                total_sum+=(largest-smallest)
        return total_sum
        