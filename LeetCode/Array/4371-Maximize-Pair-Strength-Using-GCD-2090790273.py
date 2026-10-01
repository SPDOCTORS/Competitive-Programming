class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        n=len(nums)
        maxi=0
        for i in range(n):
            for j in range(i+1,n):
                power=(nums[i]*nums[j])//self.gcd(nums[i],nums[j])**2
                if power>maxi:
                    maxi=power
        return maxi
    def gcd(self,a,b):
        while b!=0:
            a,b=b,a%b
        return a