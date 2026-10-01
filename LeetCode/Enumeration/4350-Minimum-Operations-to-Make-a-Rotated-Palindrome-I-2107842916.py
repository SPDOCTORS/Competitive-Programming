class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        ans=float('inf')
        for r in range(n):
            cost=0
            for i in range(n//2):
                j=n-i-1
                left_i=(i+r)%n
                right_i=(j+r)%n
                left=ord(s[left_i])
                right=ord(s[right_i])
                pair=min((left-right)%26,(right-left)%26)
                cost+=pair
            total=r+cost
            ans=min(total,ans)
        return ans
        