class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        freq={}
        maxi=-1
        for i in range(0,n-k+1):
            windows=set(nums[i:i+k])
            for num in windows:
                freq[num]=freq.get(num,0)+1
        for num in freq.keys():
            if freq[num]==1:
                maxi=max(maxi,num)
        return maxi

        