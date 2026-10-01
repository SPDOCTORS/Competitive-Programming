class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
        multiple=k
        for i in range(n):
            if nums[i]==multiple:
                multiple+=k
        return multiple
        