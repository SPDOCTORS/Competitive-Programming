from math import gcd
class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        n=len(nums)
        maxi=0
        for j in range(-1,n):
            if j==-1:
                arr=nums
            else:
                arr=nums[:j]+nums[j+1:]
            m = len(arr)
            score = 0
            if m <= 1:
                maxi = max(maxi, score)
                continue
            prefix = [0] * m
            suffix = [0] * m
            prefix[0] = arr[0]
            suffix[m - 1] = arr[m - 1]
            for i in range(1, m):
                prefix[i] = gcd(prefix[i - 1], arr[i])
            for i in range(m - 2, -1, -1):
                suffix[i] = gcd(suffix[i + 1], arr[i])
            for i in range(m - 1):
                if prefix[i] == suffix[i + 1]:
                    score += 1
            maxi = max(maxi, score)

        return maxi


        