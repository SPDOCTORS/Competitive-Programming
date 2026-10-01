class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        hash=[-1]*256
        l,r,maxi=0,0,0
        while r<n:
            if hash[ord(s[r])]!=-1:
                l=max(hash[ord(s[r])]+1,l)
            maxi=max(maxi,r-l+1)
            hash[ord(s[r])]=r 
            r+=1
        return maxi
        