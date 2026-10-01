class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        n=len(nums)
        nums.sort()
        longest=1
        lastsmall=float('-inf')
        cnt=1
        for i in range(n):
            if nums[i]-1==lastsmall:
                cnt+=1
                lastsmall=nums[i]
            elif nums[i]!=lastsmall:
                cnt=1
                lastsmall=nums[i]
            longest=max(longest,cnt)
        return longest


        