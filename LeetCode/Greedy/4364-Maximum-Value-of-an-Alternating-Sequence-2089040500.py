class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n==1:
            return s
        maxi=n//2
        dec=maxi-1
        return s+maxi*m-dec

        