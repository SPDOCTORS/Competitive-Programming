class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set(nums)
        for num in nums:
            s.add(num)
        s_u=sorted(s)
        for i in range(len(s_u)):
            nums[i]=s_u[i]
        return len(s_u)
        