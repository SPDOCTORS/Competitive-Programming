class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        for i in range(len(nums)):
            n=nums[i]
            sum=0
            while n>0:
                digit=n%10
                sum=sum+digit
                n=n//10
            if sum==i:
                return i
        return -1
        