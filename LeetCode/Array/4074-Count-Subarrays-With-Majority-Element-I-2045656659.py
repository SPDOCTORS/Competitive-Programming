class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n=len(nums) 
        ele=0
        for i in range(n):
            cnt=0
            for j in range(i,n):
                if nums[j]==target:
                    cnt+=1
                else: 
                    cnt-=1
                if cnt>0:
                    ele+=1
        return ele
     