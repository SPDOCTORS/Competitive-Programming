from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        mpp=defaultdict(int)
        for num in nums:
            mpp[num]+=1
        for num,cnt in mpp.items():
            if cnt>(n//2):
                return num
        return -1
    

        