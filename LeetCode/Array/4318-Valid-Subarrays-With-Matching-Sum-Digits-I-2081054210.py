class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        ans=0
        n=len(nums)
        for i in range(n):
            sum=0
            for j in range(i,n):
                sum+=nums[j]
                sumi=str(sum)
                if int(sumi[0])==x and int(sumi[-1])==x:
                    ans+=1
        return ans
            
