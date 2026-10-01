
class Solution:
    def GCD(self,a,b):
        while b!=0:
            a,b=b,a%b
        return a
    def findGCD(self, nums: List[int]) -> int:
        maxi=max(nums)
        mini=min(nums)
        return self.GCD(maxi,mini)
        