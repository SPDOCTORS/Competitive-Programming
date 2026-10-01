class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        def helper(i, count):
            if count > 1:
                return False

            if i == n:
                return True

            if nums[i] > nums[(i + 1) % n]:
                count += 1

            return helper(i + 1, count)

        return helper(0, 0)
    