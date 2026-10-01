class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x=abs(x)
        copy=x
        revNum=0
        while x>0:
            lastDigit=x%10
            revNum=revNum*10+lastDigit
            x=x//10
        return copy== revNum
        