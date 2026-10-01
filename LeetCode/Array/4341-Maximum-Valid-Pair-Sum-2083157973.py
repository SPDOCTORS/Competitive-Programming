class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        ans=float('-inf')
        maxi=nums[0]
        for j in range(k,len(nums)):
            maxi=max(maxi,nums[j-k])
            ans=max(ans,maxi+nums[j])
        return ans
        