from math import gcd
class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        def getScore(arr):
            m = len(arr)
            if m <= 1:
                return 0
            score = 0
            prefix = [0] * m
            suffix = [0] * m
            prefix[0] = arr[0]
            suffix[m - 1] = arr[m-1]
            for i in range(1, m):
                prefix[i] = gcd(prefix[i-1],arr[i])
            for i in range(m - 2, -1, -1):
                suffix[i] = gcd(suffix[i+1],arr[i])
            for i in range(m - 1):
                if prefix[i]==suffix[i+1]:
                    score += 1
            return score
        n=len(nums)
        maxi=getScore(nums)
        for j in range(n):
            arr = nums[:j]+nums[j+1:]
            score = getScore(arr)
            maxi = max(maxi,score)
        return maxi
        