class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign=-1
        else:
            sign=1
        x=abs(x)
        revNum=0
        while x>0:
            lastDigit=x%10
            revNum=revNum*10+lastDigit
            x=x//10
        revNum= revNum * sign
        if revNum<-2**31 or revNum> 2**31-1:
            return 0
        return revNum
        