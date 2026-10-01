class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums=[]
        for row in grid:
            for num in row:
                nums.append(num)
        n = len(nums)
        SN = (n * (n + 1)) // 2
        SN2 = (n * (n + 1) * (2 * n + 1)) // 6
        S = sum(nums)
        S2 = sum(num * num for num in nums)
        val1 = S - SN
        val2 = S2 - SN2
        val2 //= val1
        x = (val1 + val2) // 2
        y = x - val1
        return [int(x), int(y)]


        