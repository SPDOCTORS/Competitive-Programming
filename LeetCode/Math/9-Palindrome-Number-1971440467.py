class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        x=abs(x)
        copy=x
        rev=0
        while x>0:
            lastdigit=x%10
            rev=rev*10+lastdigit
            x//=10
        return rev==copy
        
        