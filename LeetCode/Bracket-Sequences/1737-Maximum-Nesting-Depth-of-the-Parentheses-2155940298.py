class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=0
        cur=0
        for ch in s:
            if ch=="(":
                cur+=1
                maxi=max(maxi,cur)
            elif ch==")":
                cur-=1
        return maxi
