import math
class Solution:
    def helpv(self,nums,threshold):
        sumv=0
        for num in nums:
            sumv+=math.ceil(num/threshold)
        return sumv
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        if n>threshold:
            return -1
        low,high=1,max(nums)
        while low<=high:
            mid=low+(high-low)//2
            if self.helpv(nums,mid)<=threshold:
                high=mid-1
            else:
                low=mid+1
        return low
        