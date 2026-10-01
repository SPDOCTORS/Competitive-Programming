class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)
        mid=n//2
        s=list(s)
        left=sorted(s[:mid])
        for i in range(mid):
            s[i]=left[i]
            s[n-i-1]=left[i]
        return "".join(s)
        