class Solution:
    def gcd(self,a,b):
        while b!=0:
            a,b=b,a%b
        return a
    def gcdOfOddEvenSums(self, n: int) -> int:
        return self.gcd(n*n,n*(n+1))
        
