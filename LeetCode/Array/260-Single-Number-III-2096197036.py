class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans=[]
        mpp={}
        for num in nums:
            if num in mpp:
                mpp[num]+=1
            else:
                mpp[num]=1
        for key,value in mpp.items():
            if value==1:
                ans.append(key)
        return ans

        