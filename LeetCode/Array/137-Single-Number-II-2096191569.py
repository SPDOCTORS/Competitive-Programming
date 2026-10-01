class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mpp={}
        for num in nums:
            if num in mpp:
                mpp[num]+=1
            else:
                mpp[num]=1
        for key,value in mpp.items():
            if value==1:
                return key
        return -1
        