class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k):
            l=0
            count=0
            freq={}
            count=0
            for r in range(len(nums)):
                if nums[r] in freq:
                    freq[nums[r]]+=1
                else:
                    freq[nums[r]]=1
                while len(freq)>k:
                    freq[nums[l]]-=1
                    if freq[nums[l]]==0:
                        del freq[nums[l]]
                    l+=1
                count+=r-l+1
            return count 
        return atmost(k)- atmost(k-1)


        