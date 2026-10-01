class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left=0
        n=len(nums)
        freq={}
        ans=0
        maxi=float('-inf')
        for right in range(n):
            if nums[right] not in freq:
                freq[nums[right]]=1
            else:
                freq[nums[right]]+=1
            while freq[nums[right]]>k:
                freq[nums[left]]-=1
                left+=1
            current=right-left+1
            ans=max(ans,current)
        return ans
        