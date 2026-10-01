class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        maxi1=-1000
        maxi2=-1000
        maxi3=-1000
        mini1=0
        mini2=0
        for ele in nums:
            if ele>=maxi1:
                maxi3=maxi2
                maxi2=maxi1
                maxi1=ele
            elif ele>=maxi2:
                maxi3=maxi2
                maxi2=ele
            elif ele>=maxi3:
                maxi3=ele
            
            if ele<mini1:
                mini2=mini1
                mini1=ele
            elif ele<mini2:
                mini2=ele
        return max(maxi1*maxi2*maxi3,mini1*mini2*maxi1)
        
            
    
            


        