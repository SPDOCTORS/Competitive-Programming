class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp = {}
        n = len(nums)
        for i in range(n):
            num = nums[i]
            more_needed = target - num
            if more_needed in mpp:
                return [mpp[more_needed], i]
            mpp[num] = i
        return [-1, -1]
        