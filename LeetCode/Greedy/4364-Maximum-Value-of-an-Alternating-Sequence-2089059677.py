class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n==1:
            return s
        peak=n//2
        return s+m+(peak-1)*(m-1)

        