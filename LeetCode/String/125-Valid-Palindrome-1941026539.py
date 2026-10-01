class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        return self.checkPalindrome(s, 0, len(s) - 1)

    def checkPalindrome(self, s: str, left: int, right: int) -> bool:
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return self.checkPalindrome(s, left + 1, right - 1)
    
        