class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sumi=sum(nums)
        nini=(n*(n+1))//2
        miss=nini-sumi
        return miss
        