class Solution:
    def selfpow(self,x,n):
        if n==0:
            return 1
        if n==1:
            return x
        if n%2==0:
            return self.selfpow(x*x,n//2)
        if n%2==1:
            return x*self.selfpow(x,n-1)
    def myPow(self, x: float, n: int) -> float:
        temp=n
        if temp<0:
            return 1.0/self.selfpow(x,-n)
        return self.selfpow(x,n)

        