class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = [-1, -1]
        eleIndex = []
        for i in range(len(nums)):
            eleIndex.append([nums[i], i])
        eleIndex.sort(key=lambda x: x[0])
        left, right = 0, n - 1
        while left < right:
            sum_val = eleIndex[left][0] + eleIndex[right][0]
            if sum_val == target:
                ans[0] = eleIndex[left][1]
                ans[1] = eleIndex[right][1]
                return ans
            elif sum_val < target:
                left += 1
            else:
                right -= 1
        return ans
        