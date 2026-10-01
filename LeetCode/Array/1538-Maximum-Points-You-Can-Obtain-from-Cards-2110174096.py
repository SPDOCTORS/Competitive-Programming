class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l=0
        r=0
        maxl=0
        n=len(cardPoints)
        for i in range(k):
            l=l+cardPoints[i]
            maxl=l
        right=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            l=l-cardPoints[i]
            r=r+cardPoints[right]
            right-=1
            maxl=max(maxl,l+r)
        return maxl
        