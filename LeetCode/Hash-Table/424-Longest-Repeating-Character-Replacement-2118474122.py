class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxl=0
        maxi=0
        l,r=0,0
        hash=[0]*26
        while r<len(s):
            hash[ord(s[r])-ord('A')]+=1
            maxi=max(maxi,hash[ord(s[r])-ord('A')])
            if (r-l+1)-maxi>k:
                hash[ord(s[l])-ord('A')]-=1
                l+=1
            maxl=max(maxl,r-l+1)
            r+=1
        return maxl