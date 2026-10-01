class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=0
        sum=0
        n=str(n)
        for ch in n:
            if int(ch)==0:
                pass
            else:
                sum+=int(ch)
                x=x*10+int(ch)
        return x*sum
            
