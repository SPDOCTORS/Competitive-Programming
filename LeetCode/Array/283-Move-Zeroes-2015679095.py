class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        temp=[]
        cnt=0
        for i in range(len(nums)):
            if nums[i]!=0:
                temp.append(nums[i])
                cnt+=1
        for i in range(cnt):
            nums[i]=temp[i]
        for i in range(cnt,len(nums)):
            nums[i]=0