class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=len(gain)
        sum=0
        maxi=0
        for i in range(n):
            sum+=gain[i]
            maxi=max(maxi,sum)
        return maxi

        