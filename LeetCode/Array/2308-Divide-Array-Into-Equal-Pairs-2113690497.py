class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq={}
        for x in nums:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
        for count in freq.values():
            if count%2==1:
                return False
        return True
        