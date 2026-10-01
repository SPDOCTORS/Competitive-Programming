class Solution:
    def lowb(self,nums,target):
        low,high=0,len(nums)-1
        first=-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                first=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return first
    def uppb(self,nums,target):
        low,high=0,len(nums)-1
        last=-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                last=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return last
            

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=self.lowb(nums,target)
        if first==-1:
            return [-1,-1]
        last=self.uppb(nums,target)
        return [first,last]
        