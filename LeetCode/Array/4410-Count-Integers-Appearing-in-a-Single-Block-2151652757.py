class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        mp={}
        n=len(nums)
        for i in range(n-1):
            if nums[i]!=nums[i+1]:
                mp[nums[i]]=mp.get(nums[i],0)+1
        mp[nums[-1]]=mp.get(nums[-1],0)+1 
        cnt=0
        for value in mp.values():
            if value==1:
                cnt+=1
        return cnt       