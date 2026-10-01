class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        maxcons=0
        for num in nums:
            if num==1:
                cnt+=1
                maxcons=max(maxcons,cnt)
            else:
                cnt=0
        return maxcons
        