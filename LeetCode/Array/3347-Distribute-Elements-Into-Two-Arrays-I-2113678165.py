class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums1=[0]*n
        nums1[0]=nums[0]
        nums1[n-1]=nums[1]
        id,rev=0,n-1
        for i in range(2,n):
            if nums1[id]>nums1[rev]:
                id+=1
                nums1[id]=nums[i]
            else:
                rev-=1
                nums1[rev]=nums[i]
        l,r=rev,n-1
        while l<r:
            nums1[l],nums1[r]=nums1[r],nums1[l]
            l+=1
            r-=1
        return nums1