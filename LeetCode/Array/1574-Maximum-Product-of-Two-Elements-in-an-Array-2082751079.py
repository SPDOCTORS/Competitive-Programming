class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if (nums[i]-1)*(nums[j]-1)>=maxi:
                    maxi=(nums[i]-1)*(nums[j]-1)
        return maxi
        