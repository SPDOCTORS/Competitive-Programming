class Solution:
    MOD=10**9+7
    def mypow(self,base,exp):
        ans=1
        while exp>0:
            if exp%2==1:
                ans=(ans*base)%self.MOD
            base=(base*base)%self.MOD
            exp//=2
        return ans

    def countGoodNumbers(self, n: int) -> int:
        even=(n+1)//2
        odd=n//2
        return (self.mypow(5,even)*self.mypow(4,odd))%self.MOD

        